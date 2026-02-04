// SPDX-License-Identifier: MIT

pragma solidity >=0.8.2 <0.9.0;

contract MessageDeliveredStandaloneContract {

    string private constant SIGMA_VERSION = "v4.0.0";

    enum Operation { INSERT }
    event Delta(Event e);

    struct Asset {
        bytes value;
        bytes32 hash;
    }

    struct Data {
        string key;
        Asset asset;
    }

    struct Event {
        string delta;
        Operation operation;
        Data data;
    }

    struct MessageDelivered {
        string deliveredDate;
        string messageHash;
        string receiver; 
        string fileTypeCode;
        string sourceSystem;        
    }

    string private constant MESSAGE_DELIVERED_ASSET_SCHEMA = '{"mutations":{"createMessage":{"args":{"id":"String!","deliveredDate":"String!","messageHash":"String!","receiver":"String!","fileTypeCode":"String!","sourceSystem":"String!"},"type":"Void"}},"queries":{},"rootType":"MessageDelivered","types":{"MessageDelivered":{"deliveredDate":"String!","messageHash":"String!","receiver":"String!","fileTypeCode":"String!","sourceSystem":"String!"}}}';

    function getAssetSchema() public pure returns(string memory) {
        return MESSAGE_DELIVERED_ASSET_SCHEMA;
    }

    function createMessage(
        string calldata id,
        string calldata deliveredDate, 
        string calldata messageHash, 
        string calldata receiver,
        string calldata fileTypeCode, 
        string calldata sourceSystem
        ) 
        external returns(string memory) {

        MessageDelivered memory message = MessageDelivered({
            deliveredDate: deliveredDate,
            messageHash: messageHash,
            receiver: receiver,
            fileTypeCode: fileTypeCode,
            sourceSystem: sourceSystem
        });

        Asset memory asset = buildAsset(id, abi.encode(message));
        emitEvent(Operation.INSERT, id, asset);  

        return id;   
    }

    function emitEvent(Operation op, string memory id, Asset memory asset) private {
        Event memory e = buildEvent(op, id, asset);
        emit Delta(e);
    }

    function buildAsset(string memory id, bytes memory value) private pure returns(Asset memory) {
        return Asset({
            value: value,
            hash: computeHash(id, value)
        });
    }

    function buildEvent(Operation op, string memory id, Asset memory value) private pure returns(Event memory) {       
        return Event({
            delta: SIGMA_VERSION,
            operation: op,
            data: Data({
                key: id,
                asset: value
            })
        });
    }

    function computeHash(string memory id, bytes memory rawAssetValue) private pure returns (bytes32) {
        return sha256(abi.encodePacked(id, rawAssetValue));
    }
}
