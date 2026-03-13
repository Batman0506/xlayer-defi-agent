"""
XLayer DeFi AI Agent
Main entry point
"""

import asyncio
from src.agent import DefiAgent
from src.xlayer_client import XLayerClient

async def main():
    print("🤖 XLayer DeFi AI Agent Starting...")
    
    # Initialize X Layer client
    client = XLayerClient()
    
    # Initialize Agent
    agent = DefiAgent(client)
    
    # Example commands
    commands = [
        "Swap 100 USDT to OKB",
        "Show my portfolio",
        "Stake OKB for rewards",
    ]
    
    for cmd in commands:
        print(f"\n📝 Command: {cmd}")
        result = await agent.execute(cmd)
        print(f"✅ Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
