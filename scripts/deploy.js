const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying contracts to X Layer...");

  // Deploy Staking
  const XLayerStaking = await hre.ethers.getContractFactory("XLayerStaking");
  
  // OKB and USDT addresses on X Layer
  const stakingToken = "0x0000000000000000000000000000000000000000"; // OKB (native)
  const rewardToken = "0x1D4EcF0540E7ad7B3C08F4e92Bf6D9270218A876"; // USDT

  const staking = await XLayerStaking.deploy(stakingToken, rewardToken);
  await staking.deployed();

  console.log("✅ XLayerStaking deployed to:", staking.address);

  // Save deployment info
  const deploymentInfo = {
    network: hre.network.name,
    chainId: hre.network.config.chainId,
    staking: staking.address,
    deployer: (await hre.ethers.getSigners())[0].address,
    timestamp: new Date().toISOString()
  };

  console.log("\n📋 Deployment Info:");
  console.log(JSON.stringify(deploymentInfo, null, 2));
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
