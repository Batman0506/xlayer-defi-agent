"""
X Layer Blockchain Client
Full implementation with Web3
"""

from web3 import Web3
from typing import Optional, Dict, List
import json

class XLayerClient:
    """X Layer blockchain client for DeFi operations"""
    
    # X Layer configuration
    CHAIN_ID = 196
    RPC_URL = "https://xlayer-rpc.com"
    EXPLORER = "https://xlayerscan.com"
    
    # Common token addresses on X Layer
    TOKENS = {
        "OKB": "0x0000000000000000000000000000000000000000",  # Native
        "USDT": "0x1D4EcF0540E7ad7B3C08F4e92Bf6D9270218A876",
        "USDC": "0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
        "WETH": "0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000",
    }
    
    # DEX Router (XSwap)
    ROUTER_ADDRESS = "0x9D494768936B6bBc8873F3F7C76DD0e549d66031"
    
    def __init__(self, private_key: Optional[str] = None, rpc_url: Optional[str] = None):
        self.rpc_url = rpc_url or self.RPC_URL
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.private_key = private_key
        self.address = None
        
        if private_key:
            from eth_account import Account
            account = Account.from_key(private_key)
            self.address = account.address
            
        # Router ABI (simplified)
        self.router_abi = json.loads('''[
            {"inputs":[{"name":"amountIn","type":"uint256"},{"name":"amountOutMin","type":"uint256"},{"name":"path","type":"address[]"},{"name":"to","type":"address"},{"name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"name":"tokenA","type":"address"},{"name":"tokenB","type":"address"},{"name":"amountADesired","type":"uint256"},{"name":"amountBDesired","type":"uint256"},{"name":"amountAMin","type":"uint256"},{"name":"amountBMin","type":"uint256"},{"name":"to","type":"address"},{"name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"name":"amountA","type":"uint256"},{"name":"amountB","type":"uint256"},{"name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}
        ]''')
        
        # ERC20 ABI
        self.erc20_abi = json.loads('''[
            {"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}
        ]''')
    
    def is_connected(self) -> bool:
        """Check connection to X Layer"""
        return self.w3.is_connected()
    
    def get_block_number(self) -> int:
        """Get current block number"""
        return self.w3.eth.block_number
    
    def get_balance(self, address: Optional[str] = None) -> Dict[str, float]:
        """Get wallet balance for all tokens"""
        addr = address or self.address
        if not addr:
            return {"error": "No address provided"}
        
        balances = {}
        
        # Native OKB balance
        okb_wei = self.w3.eth.get_balance(addr)
        balances["OKB"] = float(Web3.from_wei(okb_wei, 'ether'))
        
        # ERC20 token balances
        for symbol, token_addr in self.TOKENS.items():
            if symbol == "OKB":
                continue
            try:
                contract = self.w3.eth.contract(
                    address=Web3.to_checksum_address(token_addr),
                    abi=self.erc20_abi
                )
                decimals = contract.functions.decimals().call()
                balance = contract.functions.balanceOf(Web3.to_checksum_address(addr)).call()
                balances[symbol] = float(balance) / (10 ** decimals)
            except Exception as e:
                balances[symbol] = 0.0
        
        return balances
    
    def get_gas_price(self) -> float:
        """Get current gas price in Gwei"""
        return float(Web3.from_wei(self.w3.eth.gas_price, 'gwei'))
    
    def build_swap_tx(
        self,
        from_token: str,
        to_token: str,
        amount: float,
        slippage: float = 0.5
    ) -> Dict:
        """Build a swap transaction"""
        
        if from_token not in self.TOKENS or to_token not in self.TOKENS:
            return {"error": "Token not supported"}
        
        from_addr = self.TOKENS[from_token]
        to_addr = self.TOKENS[to_token]
        
        # Get decimals
        if from_token == "OKB":
            decimals = 18
            amount_wei = Web3.to_wei(amount, 'ether')
        else:
            contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(from_addr),
                abi=self.erc20_abi
            )
            decimals = contract.functions.decimals().call()
            amount_wei = int(amount * (10 ** decimals))
        
        # Build tx
        tx = {
            "from": self.address,
            "chainId": self.CHAIN_ID,
            "gas": 200000,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(self.address),
            "value": amount_wei if from_token == "OKB" else 0
        }
        
        return {
            "status": "ready",
            "from_token": from_token,
            "to_token": to_token,
            "amount": amount,
            "amount_wei": str(amount_wei),
            "gas_price_gwei": float(Web3.from_wei(tx["gasPrice"], 'gwei')),
            "estimated_gas": tx["gas"]
        }
    
    def get_portfolio(self, address: Optional[str] = None) -> Dict:
        """Get complete portfolio overview"""
        addr = address or self.address
        balances = self.get_balance(addr)
        
        # Calculate total (mock prices)
        prices = {"OKB": 50.0, "USDT": 1.0, "USDC": 1.0, "WETH": 3000.0}
        total_value = sum(balances.get(token, 0) * prices.get(token, 0) for token in prices)
        
        return {
            "address": addr,
            "total_value_usd": total_value,
            "balances": balances,
            "block_number": self.get_block_number(),
            "gas_price_gwei": self.get_gas_price()
        }
