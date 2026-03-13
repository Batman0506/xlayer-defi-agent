# XLayer DeFi Smart Contracts

## Contracts

### 1. XLayerStaking.sol
Staking contract with 15.5% APY.

**Features:**
- Stake any ERC20 token
- Auto-calculate rewards
- Claim rewards anytime

**Deployment:**
```bash
# Deploy to X Layer Testnet
npx hardhat run scripts/deploy-staking.js --network xlayer-testnet
```

### 2. SimpleSwap.sol
Basic AMM swap contract.

**Features:**
- Token pair creation
- Liquidity provision
- Token swaps

## Testing

```bash
npx hardhat test
```

## Deployment

1. Copy `.env.example` to `.env`
2. Add your private key and RPC URL
3. Run:
```bash
npx hardhat run scripts/deploy.js --network xlayer
```
