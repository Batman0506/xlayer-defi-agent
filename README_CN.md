# 🤖 XLayer DeFi AI Agent 中文文档

> 专为 X Layer 区块链打造的 AI DeFi 助手 - X Layer AI Agent Builder 激励计划参赛项目

[![GitHub](https://img.shields.io/badge/GitHub-Batman0506-blue)](https://github.com/Batman0506/xlayer-defi-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 项目简介

**XLayer DeFi AI Agent** 是一个智能 DeFi 助手，让用户用自然语言即可与 X Layer 区块链交互。

### 核心功能

- 🎙️ **自然语言控制**：说"兑换 100 USDT 成 OKB"即可自动执行交易
- 🔄 **代币交换**：集成 DEX，实时报价，快速交易
- 💰 **质押挖矿**：质押代币赚取收益（年化 15.5%）
- 📊 **资产看板**：实时追踪所有资产和持仓
- ⛽ **Gas 费用**：实时查询 X Layer 网络费用
- 📜 **智能合约**：Solidity 合约支持链上操作

## 技术栈

- **区块链**：X Layer（Chain ID: 196，兼容 EVM）
- **智能合约**：Solidity 0.8.19
- **后端**：Python 3.10，Web3.py
- **AI**：自然语言处理（NLP）命令解析
- **部署**：Hardhat

## X Layer 简介

**X Layer** 是由 X（原 Twitter）和 OKX 联合推出的比特币二层网络：

- ✅ **比特币 L2**：继承比特币安全性
- ✅ **EVM 兼容**：以太坊生态无缝迁移
- ✅ **低 Gas 费**：交易成本低
- ✅ **高性能**：快速确认

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/Batman0506/xlayer-defi-agent.git
cd xlayer-defi-agent

# 安装依赖
pip install -r requirements.txt

# 配置环境
cp .env.example .env
# 编辑 .env 填入私钥和 API 密钥

# 运行
python main.py
```

## 使用示例

```python
from src.agent import DefiAgent
from src.xlayer_client import XLayerClient

# 初始化
client = XLayerClient(private_key="你的私钥")
agent = DefiAgent(client)

# 执行命令
await agent.execute("兑换 100 USDT 成 OKB")
await agent.execute("查看我的资产")
await agent.execute("质押 50 OKB")
```

## 支持的命令

| 命令 | 示例 | 说明 |
|------|------|------|
| 兑换 | "Swap 100 USDT to OKB" | DEX 代币交换 |
| 质押 | "Stake 50 OKB" | 质押赚取收益 |
| 资产 | "Show my portfolio" | 查看资产余额 |
| Gas | "Gas price" | 查询 Gas 费用 |
| 帮助 | "Help" | 显示帮助信息 |

## X Layer 配置

| 网络 | Chain ID | RPC 地址 |
|------|----------|----------|
| 主网 | 196 | https://xlayer-rpc.com |
| 测试网 | 195 | https://testnet-rpc.xlayer.tech |
| 浏览器 | - | https://xlayerscan.com |

## 智能合约

### XLayerStaking.sol - 质押合约

质押代币赚取收益的 Solidity 合约。

```solidity
// 质押代币
function stake(uint256 _amount) external

// 解除质押
function unstake(uint256 _amount) external

// 领取奖励
function claimReward() external

// 查询质押信息
function getStakeInfo(address _user) external view
```

**特点：**
- 15.5% 年化收益率
- 随时解质押
- 自动计算奖励

### SimpleSwap.sol - 兑换合约

基础 AMM 兑换合约框架。

### 部署

```bash
# 安装依赖
npm install

# 部署到 X Layer 测试网
npx hardhat run scripts/deploy.js --network xlayer-testnet
```

## 项目结构

```
xlayer-defi-agent/
├── src/
│   ├── agent.py           # AI Agent（NLP 命令解析）
│   └── xlayer_client.py   # X Layer Web3 客户端
├── contracts/
│   ├── DefiStaking.sol    # 质押合约（15.5% APY）
│   └── SimpleSwap.sol     # DEX 兑换合约
├── scripts/
│   └── deploy.js          # 部署脚本
├── main.py                # 演示入口
├── hardhat.config.js      # Hardhat 配置
├── requirements.txt       # Python 依赖
└── README.md / README_CN.md  # 文档
```

## 激励计划

本项目参加 [X Layer AI Agent Builder 激励计划](https://x.com/XLayerOfficial)

**奖金池：200,000 USDT**

- 🏗️ 在 X Layer 上构建创新 AI Agent
- 📖 开源你的项目
- 📱 在 X 上分享进度
- 💰 赢取奖金！

## 路线图

- [x] 项目初始化
- [x] 核心 Agent 功能
- [x] 智能合约开发
- [ ] 部署到 X Layer 测试网
- [ ] 集成更多 DEX
- [ ] Web 界面
- [ ] Telegram 机器人

## 许可证

MIT © 2026 @xiaogaoyayou

---

用 🤖 为 X Layer 生态赋能

**X Layer**：由 X（Twitter）驱动的首个比特币二层网络
