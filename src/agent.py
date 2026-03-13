"""
DeFi AI Agent
Natural language to DeFi actions
"""

import re
from typing import Dict, Any, Optional
from .xlayer_client import XLayerClient

class DefiAgent:
    """AI Agent for DeFi operations on X Layer"""
    
    def __init__(self, client: XLayerClient, ai_api_key: Optional[str] = None):
        self.client = client
        self.ai_api_key = ai_api_key
        self.conversation_history = []
        
    async def execute(self, command: str) -> str:
        """Execute natural language command"""
        self.conversation_history.append({"role": "user", "content": command})
        
        command_lower = command.lower()
        
        if any(word in command_lower for word in ["swap", "exchange", "trade", "换"]):
            return await self._handle_swap(command)
        
        elif any(word in command_lower for word in ["balance", "portfolio", "余额", "资产"]):
            return await self._handle_balance()
        
        elif any(word in command_lower for word in ["stake", "staking", "质押", "挖矿"]):
            return await self._handle_stake(command)
        
        elif any(word in command_lower for word in ["gas", "fee", "费用"]):
            return await self._handle_gas()
        
        elif any(word in command_lower for word in ["help", "帮助"]):
            return self._get_help()
        
        else:
            return self._get_help()
    
    async def _handle_swap(self, command: str) -> str:
        patterns = [
            r'swap\s+(\d+)\s+([a-zA-Z]+)\s+(?:to|for)\s+([a-zA-Z]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                amount = float(match.group(1))
                from_token = match.group(2).upper()
                to_token = match.group(3).upper()
                
                tx_info = self.client.build_swap_tx(from_token, to_token, amount)
                
                if "error" in tx_info:
                    return f"Error: {tx_info['error']}"
                
                return (
                    f"Swap Ready\n\n"
                    f"From: {amount} {from_token}\n"
                    f"To: {to_token}\n"
                    f"Gas Price: {tx_info['gas_price_gwei']:.2f} Gwei\n"
                    f"Estimated Gas: {tx_info['estimated_gas']}"
                )
        
        return "Could not parse swap command. Try: 'Swap 100 USDT to OKB'"
    
    async def _handle_balance(self) -> str:
        portfolio = self.client.get_portfolio()
        
        if "error" in portfolio:
            return f"Error: {portfolio['error']}"
        
        balances = portfolio['balances']
        lines = [f"Portfolio - {portfolio['address'][:10]}...", ""]
        
        for token, balance in balances.items():
            if balance > 0:
                lines.append(f"{token}: {balance:.4f}")
        
        lines.append("")
        lines.append(f"Total Value: ${portfolio['total_value_usd']:.2f}")
        
        return "\n".join(lines)
    
    async def _handle_stake(self, command: str) -> str:
        match = re.search(r'stake\s+(?:(\d+)\s+)?([a-zA-Z]+)', command, re.IGNORECASE)
        
        if match:
            amount = float(match.group(1)) if match.group(1) else None
            token = match.group(2).upper()
            
            if amount:
                return f"Staking {amount} {token} - APY 15.5%"
            else:
                return f"Available pools:\nOKB Staking - 15.5% APY\nUSDT LP - 8.2% APY"
        
        return "Could not parse stake command"
    
    async def _handle_gas(self) -> str:
        gas_price = self.client.get_gas_price()
        return f"Current Gas Price: {gas_price:.2f} Gwei"
    
    def _get_help(self) -> str:
        return (
            "XLayer DeFi AI Agent Commands:\n"
            "- Swap [amount] [token] to [token]\n"
            "- Show balance/portfolio\n"
            "- Stake [amount] [token]\n"
            "- Gas price\n"
            "- Help"
        )
    
    def get_status(self) -> Dict[str, Any]:
        return {
            "connected": self.client.is_connected(),
            "chain_id": self.client.CHAIN_ID,
            "address": self.client.address
        }
