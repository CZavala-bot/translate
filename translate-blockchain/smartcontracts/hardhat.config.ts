import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

const config: HardhatUserConfig = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
      viaIR: true, 
    },
  },
  sourcify: {
    enabled: true
  },
  networks: {
    // in built test network to use when developing contracts
    hardhat: {
      chainId: 1337
    },
    quorumlocal: {
      url: "http://127.0.0.1:8545",
      chainId: 1337,
      // test accounts only, all good ;)
      accounts: [
        "0x8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63",
        "0xc87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3",
        "0xae6ae8e5ccbfb04590405997ee2d52d2b330726137b875053c36d94e974d162f"
      ]
    },
    quorum_infoport: {
      url: "http://172.29.110.49:8545",
      chainId: 1337,
      // test accounts only, all good ;)
      accounts: [
        "0x8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63",
        "0xc87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3",
        "0xae6ae8e5ccbfb04590405997ee2d52d2b330726137b875053c36d94e974d162f"
      ]
    }
  },
  etherscan: {
    apiKey: {
      'quorum_infoport': 'empty'
    },
    customChains: [
      {
        network: "quorum_infoport",
        chainId: 1337,
        urls: {
          apiURL: "http://172.29.110.49:26000/api",
          browserURL: "http://172.29.110.49:26000"
        }
      }
    ]
  }
};

export default config;
