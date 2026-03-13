# 🤖 XLayer DeFi AI Agent

> AI Agent for DeFi on X Layer - X Layer AI Agent Builder Incentive Program

[![GitHub](https://img.shields.io/badge/GitHub-Batman0506-blue)](https://github.com/Batman0506/xlayer-defi-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

An intelligent DeFi Agent that helps users interact with X Layer blockchain using natural language commands.

### Features

- 🎙️ **Natural Language**: "Swap 100 USDT to OKB" → executes transaction
- 🔄 **Swap**: DEX token swapping with real-time quotes
- 💰 **Staking**: Stake tokens and earn rewards (15.5% APY)
- 📊 **Portfolio**: Track all your assets and positions
- ⛽ **Gas**: Get current gas prices on X Layer
- 📜 **Smart Contracts**: Solidity contracts for on-chain operations

## Tech Stack

- **Blockchain**: X Layer (Chain ID: 196, EVM compatible)
- **Smart Contracts**: Solidity 0.8.19
- **Backend**: Python 3.10, Web3.py
- **AI**: NLP pattern matching for command parsing
- **Deployment**: Hardhat

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Batman0506/xlayer-defi-agent.git
cd xlayer-defi-agent

# Install Python dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your private key and API keys

# Run the agent
python main.py
```

## Usage Examples

```python
from src.agent import DefiAgent
from src.xlayer_client import XLayerClient

# Initialize
client = XLayerClient(private_key="your_key")
agent = DefiAgent(client)

# Execute commands
await agent.execute("Swap 100 USDT to OKB")
await agent.execute("Show my portfolio")
await agent.execute("Stake 50 OKB")
await agent.execute("Gas price")
```

## X Layer Configuration

| Network | Chain ID | RPC |
|---------|----------|-----|
| Mainnet | 196 | https://xlayer-rpc.com |
| Testnet | 195 | https://testnet-rpc.xlayer.tech |
| Explorer | - | https://xlayerscan.com |

## Smart Contracts

### XLayerStaking.sol

Staking contract with configurable APY.

```solidity
function stake(uint256 _amount) external
function unstake(uint256 _amount) external
function claimReward() external
function getStakeInfo(address _user) external view
```

### Deploy

```bash
# Deploy to X Layer Testnet
npm install
npx hardhat run scripts/deploy.js --network xlayer-testnet
```

## Project Structure

```
xlayer-defi-agent/
├── src/
│   ├── agent.py           # AI Agent with NLP
│   └── xlayer_client.py   # X Layer Web3 client
├── contracts/
│   ├── DefiStaking.sol    # Staking contract
│   └── SimpleSwap.sol     # DEX swap contract
├── scripts/
│   └── deploy.js          # Deployment script
├── main.py                # Demo entry point
├── hardhat.config.js      # Hardhat configuration
└── requirements.txt       # Python dependencies
```

## Grant Program

Part of [X Layer AI Agent Builder Incentive Program](https://x.com/XLayerOfficial)

**Prize Pool: 200,000 USDT**

- Build innovative AI Agents on X Layer
- Open source your project
- Share progress on X
- Win prizes!

## Roadmap

- [x] Project initialization
- [x] Core agent functionality
- [x] Smart contracts
- [ ] Deploy to X Layer testnet
- [ ] Add more DEX integrations
- [ ] Web interface
- [ ] Telegram bot

## License

MIT © 2026 @xiaogaoyayou

---

Built with 🤖 for the X Layer ecosystem

**X Layer**: The first Bitcoin L2 powered by X (Twitter)
