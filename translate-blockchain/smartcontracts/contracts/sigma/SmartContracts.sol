// SPDX-License-Identifier: MIT

pragma solidity >=0.7.4 <0.9.0;
pragma abicoder v2;

import { buildAsset, buildEvent, computeHash } from "./UtilFunctions.sol";
import { Asset, AssetHashData, AssetValueData, CrudStatement, Event, Operation } from "./DataTypes.sol";

abstract contract ISchemaContract {
    // Retrieve the data model schema for this smart-contract's assets
    function getAssetSchema() public pure virtual returns(string memory);
}

abstract contract IReadableContract is ISchemaContract {
    function readAsset(string calldata id) public view virtual returns(bytes memory);
    function assetExists(string calldata id) public view virtual returns(bool);
    function getFirstBlockNumber() public view virtual returns(uint);
}

abstract contract IWritableContract is ISchemaContract {
    function insertAsset(string memory id, bytes memory value) public virtual returns(string memory);
    function updateAsset(string memory id, bytes memory value) public virtual returns(string memory);
    function upsertAsset(string memory id, bytes memory value) public virtual returns(string memory);
    function deleteAsset(string calldata id) public virtual returns(string memory);
}

abstract contract IHashableContract is IWritableContract {
    function insertAssetValue(string memory id, bytes memory value) public virtual returns(string memory);
    function insertAssetHash (string memory id, bytes memory value) public virtual returns(string memory);
    function updateAssetValue(string memory id, bytes memory value) public virtual returns(string memory);
    function updateAssetHash (string memory id, bytes memory value) public virtual returns(string memory);
    function upsertAssetValue(string memory id, bytes memory value) public virtual returns(string memory);
    function upsertAssetHash (string memory id, bytes memory value) public virtual returns(string memory);
}

abstract contract ITransactionalContract is IWritableContract {
    function executeTransaction(CrudStatement[] memory statements) public virtual returns(string[] memory);
}

/**
 * This contract can store either full raw values or just their SHA-256 hashes,
 * associated to their identifier key, in the ledger state. These objects,
 * along with their identifier and hash, are as well contained in the contract
 * events emitted upon the execution of data modification operations.
 */
abstract contract ISigmaContract is IHashableContract, ITransactionalContract, IReadableContract {
}




/**
 * Contract which provides internal functions implementations for the ledger status
 * modification and retrieval operations. Their visibility can be turned to public
 * as desired by children contracts, or used internally by public functions implemented
 * and exposed by contracts extending this one.
 */
contract SigmaBaseContract {

    mapping(string => bytes) private ledger;

    event Delta(Event e);

    uint private blockNumber;

    constructor(){
        blockNumber = block.number;
    }

    // IWritableContract functions

    function _insertAsset(string memory id, bytes memory value, bool hashValue) internal returns(Event memory) {
        require(!_assetExists(id),
            string(abi.encodePacked("The asset to be created already exists: ", id)));
        
        Asset memory asset = buildAsset(id, value);
        Event memory e = emitEvent(Operation.INSERT, id, asset);
        putState(id, asset, hashValue);
        return e;
    }

    function _updateAsset(string memory id, bytes memory value, bool hashValue) internal returns(Event memory) {
        require(_assetExists(id),
            string(abi.encodePacked("The asset to be updated does not exist: ", id)));
        
        Asset memory asset = buildAsset(id, value);
        Event memory e = emitEvent(Operation.UPDATE, id, asset);
        putState(id, asset, hashValue);
        return e;
    }

    function _upsertAsset(string memory id, bytes memory value, bool hashValue) internal returns(Event memory) {
        Asset memory asset = buildAsset(id, value);

        // Overwrite a previous value or insert a new record depending on the asset's existence
        Event memory e = emitEvent(_assetExists(id) ? Operation.UPDATE : Operation.INSERT, id, asset);

        putState(id, asset, hashValue);
        return e;
    }

    function _deleteAsset(string memory id) internal returns(Event memory) {
        require(_assetExists(id),
            string(abi.encodePacked("The asset to be deleted does not exist: ", id)));
        
        Asset memory asset;
        Event memory e = emitEvent(Operation.DELETE, id, asset);
        deleteState(id);
        return e;
    }

    // ITransactionalContract function
    function _executeTransaction(CrudStatement[] memory statements) internal returns(string[] memory) {
        CrudStatement memory stmt;
        string[] memory affectedIds = new string[](statements.length);
        for (uint n = 0; n < statements.length; n++) {
            stmt = statements[n];
            if (Operation.INSERT == stmt.operation) {
                _insertAsset(stmt.id, stmt.value, stmt.hashValue);
            } else if (Operation.UPDATE == stmt.operation) {
                _updateAsset(stmt.id, stmt.value, stmt.hashValue);
            } else if (Operation.UPSERT == stmt.operation) {
                _upsertAsset(stmt.id, stmt.value, stmt.hashValue);
            } else if (Operation.DELETE == stmt.operation) {
                _deleteAsset(stmt.id);
            }
            affectedIds[n] = stmt.id;
        }
        return affectedIds;
    }



    // IReadableContract functions

    // Get the asset value/hash from the ledger state
    function _readAsset(string memory id) internal view returns(bytes memory) {
        return getState(id);
    }

    // If the asset (full object) value is stored, compute its hash and return it
    function _readAssetHash(string memory id) internal view returns(bytes32) {
        bytes memory assetValue = getState(id);
        return assetValue.length == 32 ?
            bytes32(assetValue) : computeHash(id, assetValue);
    }

    function _assetExists(string memory id) internal view returns(bool) {
        return getState(id).length > 0;
    }

    function _getFirstBlockNumber() internal view returns(uint) {
        return blockNumber;
    }

    // Private functions

    function getState(string memory key) private view returns(bytes memory) {
        return ledger[key];
    }

    function putState(string memory key, Asset memory valueAsset, bool hashValue) private {
        ledger[key] = hashValue ? abi.encodePacked(valueAsset.hash) : valueAsset.value;
    }

    function deleteState(string memory key) private {
        delete ledger[key];
    }

    function emitEvent(Operation op, string memory id, Asset memory asset) private returns(Event memory) {
        Event memory e = buildEvent(op, id, asset);
        emit Delta(e);
        return e;
    }
}




/**
 * Base contract for smart-contracts adhered to the Sigma specification, that actually
 * joins and aggregates the Delta and Epsilon operation interfaces.
 * It provides its own implementations for the ledger modification primitives,
 * which perform the data (hash) modification operation and also emit the corresponding event.
 * In addition, it provides convenience functions for checking whether an asset exists
 * or retrieving the hashes of all assets from the ledger.
 */
abstract contract SigmaContract is SigmaBaseContract, ISigmaContract {

    /**
     * Issue a new asset to the ledger state with the provided data.
     */
    function insertAsset(string memory id, bytes memory value) public override returns(string memory) {
        return insertAssetValue(id, value);
    }

    function insertAssetValue(string memory id, bytes memory value) public override returns(string memory) {
        _insertAsset(id, value, false);
        return id;
    }

    function insertAssetHash(string memory id, bytes memory value) public override returns(string memory) {
        _insertAsset(id, value, true);
        return id;
    }



    /**
     * Update an existing asset in the ledger with the provided data.
     */
    function updateAsset(string memory id, bytes memory value) public override returns(string memory) {
        return updateAssetValue(id, value);
    }

    function updateAssetValue(string memory id, bytes memory value) public override returns(string memory) {
        _updateAsset(id, value, false);
        return id;
    }

    function updateAssetHash(string memory id, bytes memory value) public override returns(string memory) {
        _updateAsset(id, value, true);
        return id;
    }



    /**
     * Insert or update an asset into the ledger state with the provided data.
     */
    function upsertAsset(string memory id, bytes memory value) public override returns(string memory) {
        return upsertAssetValue(id, value);
    }

    function upsertAssetValue(string memory id, bytes memory value) public override returns(string memory) {
        _upsertAsset(id, value, false);
        return id;
    }

    function upsertAssetHash(string memory id, bytes memory value) public override returns(string memory) {
        _upsertAsset(id, value, true);
        return id;
    }



    /**
     * Delete a given asset from the ledger state.
     */
    function deleteAsset(string calldata id) public override returns(string memory) {
        _deleteAsset(id);
        return id;
    }



    /**
     * Return the value/hash stored in the ledger state for the asset identified by the key provided.
     */
    function readAsset(string calldata id) public view override returns(bytes memory) {
        return _readAsset(id);
    }



    /**
     * Return whether the asset identified by the key provided exists in the ledger state.
     */
    function assetExists(string calldata id) public view override returns(bool) {
        return _assetExists(id);
    }


    function getFirstBlockNumber() public view override returns(uint) {
        return _getFirstBlockNumber();
    }

    /**
     * Execute a sequence of operations in the context of a single transaction.
     */
    function executeTransaction(CrudStatement[] memory statements) public override returns(string[] memory) {
        return _executeTransaction(statements);
    }

}
