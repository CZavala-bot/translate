import { ethers } from 'hardhat';
import * as contract from "./contract.json"

async function main() {
    const smartcontract = await ethers.getContractAt(
    contract.contractName, contract.address);

    const id = "453624cf-1783-4722-a634-585ed2b11489";
    const receivedDate = "2025-11-21T09:13:45.022Z";
    const messageHash = "a9f217105d37f04dea9222b4a5f4133f5c483d948584734f1ebcb91ff3a62c93256beee279f1da254310c66982c683de257c74e5859e61c53cfa5629d3188b5e";
    const sender = "test-sender";
    const fileTypeCode = "XML";
    const sourceSystem = "API";

    const result = await smartcontract.createMessage
    (
        id,
        receivedDate,
        messageHash,
        sender,
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
