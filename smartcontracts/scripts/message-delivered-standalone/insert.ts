import { ethers } from 'hardhat';
import * as contract from "./contract.json"

async function main() {
    const smartcontract  = await ethers.getContractAt(
        contract.contractName, 
        contract.address);
    
    createMessage(smartcontract);

}

async function createMessage(smartcontract: any) {
    const id = "385442e4-fba6-4ab9-951d-af1155f71942";
    const deliveredDate = "2025-11-21T09:16:42.991Z";
    const messageHash = "a9f217105d37f04dea9222b4a5f4133f5c483d948584734f1ebcb91ff3a62c93256beee279f1da254310c66982c683de257c74e5859e61c53cfa5629d3188b5e";
    const receiver = "test-receiver";
    const fileTypeCode = "XML";
    const sourceSystem = "API";

    const result = await smartcontract.createMessage
        (
        id,
        deliveredDate,
        messageHash,
        receiver,
        fileTypeCode,
        sourceSystem
    );
    console.log(result);
}

// We recommend this pattern to be able to use async/await everywhere and properly handle errors.
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
