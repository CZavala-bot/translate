// SPDX-License-Identifier: MIT

pragma solidity >=0.7.4 <0.9.0;
pragma abicoder v2;

import { SigmaContract } from "./sigma/SmartContracts.sol";

contract StructStringContract is SigmaContract {

    struct StructString {
        string value;
    }

    function abiUpsertAsset(string memory id, string memory value) public {
        upsertAsset(id, encodeSimpleAsset(value));
    }

    function abiDeleteAsset(string calldata id) public {
        deleteAsset(id);
    }

    function encodeSimpleAsset(string memory value) private pure returns(bytes memory) {
        return abi.encode(StructString(value));
    }

    string private constant SCHEMA = '{"types": {"StructString": {"value": "String!"}},"rootType": "StructString","queries": {},"mutations": {"abiUpsertAsset": {"args": {"id": "String!","value": "String!"},"type": "Void"},"abiDeleteAsset": {"args": {"id": "String!"},"type": "Void"}}}';

    function getAssetSchema() public pure override returns(string memory) {
        return SCHEMA;
    }
}
