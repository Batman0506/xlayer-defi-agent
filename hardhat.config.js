require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    // X Layer Mainnet
    xlayer: {
      url: "https://xlayer-rpc.com",
      chainId: 196,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : []
    },
    // X Layer Testnet
    "xlayer-testnet": {
      url: "https://testnet-rpc.xlayer.tech",
      chainId: 195,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : []
    }
  },
  etherscan: {
    apiKey: {
      xlayer: "your-xlayer-api-key"
    },
    customChains: [
      {
        network: "xlayer",
        chainId: 196,
        urls: {
          apiURL: "https://xlayerscan.com/api",
          browserURL: "https://xlayerscan.com"
        }
      }
    ]
  }
};
