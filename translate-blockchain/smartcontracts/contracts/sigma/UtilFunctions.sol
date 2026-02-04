// SPDX-License-Identifier: MIT

pragma solidity >=0.7.4 <0.9.0;

import { Asset, Data, Event, Operation } from "./DataTypes.sol";

string constant SIGMA_VERSION = "v4.0.0";

/** Utility and convenience functions. */

function buildAsset(string memory id, bytes memory value) pure returns(Asset memory) {
    Asset memory asset = Asset({
        value: value,
        hash: computeHash(id, value)
    });
    return asset;
}

function buildEvent(Operation op, string memory id, Asset memory value) pure returns(Event memory) {
    Data memory data;
    data.key = id;
    if (op != Operation.DELETE) {
        data.asset = value;
    }

    Event memory e = Event({
        delta: SIGMA_VERSION,
        operation: op,
        data: data
    });
    return e;
}

function computeHash(string memory id, bytes memory rawAssetValue) pure returns (bytes32) {
    return sha256(abi.encodePacked(id, rawAssetValue));
}

function uintArray2StringArray(uint[] memory intArray) pure returns (string[] memory) {
    string[] memory strArray = new string[](intArray.length);
    for (uint n = 0; n < intArray.length; n++) {
        strArray[n] = toString(intArray[n]);
    }
    return strArray;
}

/**
 * @dev Converts a `uint256` to its ASCII `string` decimal representation.
 */
function toString(uint256 value) pure returns (string memory) {
    unchecked {
        uint256 length = log10(value) + 1;
        string memory buffer = new string(length);
        uint256 ptr;
        /// @solidity memory-safe-assembly
        assembly {
            ptr := add(buffer, add(32, length))
        }
        while (true) {
            ptr--;
            /// @solidity memory-safe-assembly
            assembly {
                mstore8(ptr, byte(mod(value, 10), _SYMBOLS))
            }
            value /= 10;
            if (value == 0) break;
        }
        return buffer;
    }
}

bytes16 constant _SYMBOLS = "0123456789abcdef";

/**
 * @dev Return the log in base 10, rounded down, of a positive value.
 * Returns 0 if given 0.
 */
function log10(uint256 value) pure returns (uint256) {
    uint256 result = 0;
    unchecked {
        if (value >= 10 ** 64) {
            value /= 10 ** 64;
            result += 64;
        }
        if (value >= 10 ** 32) {
            value /= 10 ** 32;
            result += 32;
        }
        if (value >= 10 ** 16) {
            value /= 10 ** 16;
            result += 16;
        }
        if (value >= 10 ** 8) {
            value /= 10 ** 8;
            result += 8;
        }
        if (value >= 10 ** 4) {
            value /= 10 ** 4;
            result += 4;
        }
        if (value >= 10 ** 2) {
            value /= 10 ** 2;
            result += 2;
        }
        if (value >= 10 ** 1) {
            result += 1;
        }
    }
    return result;
}
