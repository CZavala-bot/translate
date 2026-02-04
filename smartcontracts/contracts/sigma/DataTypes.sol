// SPDX-License-Identifier: MIT

pragma solidity >=0.7.4 <0.9.0;

enum Operation { INSERT, UPDATE, UPSERT, DELETE }

struct Asset {
    bytes value;
    bytes32 hash;
}

struct Data {
    string key;
    Asset asset;
}

struct AssetValueData {
    string key;
    bytes value;
}

struct AssetHashData {
    string key;
    bytes32 valueHash;
}

struct Event {
    string delta;
    Operation operation;
    Data data;
}

struct CrudStatement {
    Operation operation;
    string id;
    bytes value;
    bool hashValue;
}
