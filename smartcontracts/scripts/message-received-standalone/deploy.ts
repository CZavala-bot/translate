import { ethers } from "hardhat"
import * as contract from "./contract.json"

async function main() {
  const QuorumToken  = await ethers.getContractFactory(contract.contractName)
  const deploy = await QuorumToken.deploy()
  console.log("Contract deploy at: %s", await deploy.getAddress());
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error)
  process.exitCode = 1
})