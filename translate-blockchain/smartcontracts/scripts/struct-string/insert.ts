import { ethers } from 'hardhat';
import * as contract from "./contract.json"

async function main() {
    const smartcontract  = await ethers.getContractAt(
        contract.contractName, 
        contract.address);
    
    const id = "1";
    const value = "cadena de ejemplo";

    const result = await smartcontract.abiUpsertAsset(id, value);
    console.log(result);
    console.log('Inserted: id', id, 'value', value);

}

// We recommend this pattern to be able to use async/await everywhere and properly handle errors.
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
