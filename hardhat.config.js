require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    ganache: {
      url: "http://127.0.0.1:7545", // Default Ganache URL
      accounts: [
        // Paste your Ganache private key here (without 0x)
        "cf2e3283f957e4bab195ec5b020f8368f947f9de898b83d71a81020dbfbdb2db"
      ]
    }
  }
};
