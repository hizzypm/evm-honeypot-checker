#!/usr/bin/env python3
"""EVM Honeypot / Token Safety Checker"""

import argparse
import os
from web3 import Web3
from colorama import Fore, init
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()

CHAINS = {
    "eth": "https://eth.llamarpc.com",
    "base": "https://mainnet.base.org",
    "arbitrum": "https://arb1.arbitrum.io/rpc",
    "bsc": "https://bsc-dataseed.binance.org",
}

def check_token(token_address: str, chain: str = "base"):
    rpc = CHAINS.get(chain, CHAINS["base"])
    w3 = Web3(Web3.HTTPProvider(rpc))
    
    if not w3.is_connected():
        print(f"{Fore.RED}Failed to connect to {chain}")
        return
    
    token = w3.to_checksum_address(token_address)
    print(f"{Fore.CYAN}Checking token: {token}")
    print(f"{Fore.CYAN}Chain: {chain}\n")
    
    abi = [
        {"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "type": "function"},
        {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"},
        {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
        {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "type": "function"},
    ]
    
    contract = w3.eth.contract(address=token, abi=abi)
    
    try:
        name = contract.functions.name().call()
        symbol = contract.functions.symbol().call()
        decimals = contract.functions.decimals().call()
        supply = contract.functions.totalSupply().call() / (10 ** decimals)
        
        print(f"{Fore.GREEN}Name: {name}")
        print(f"{Fore.GREEN}Symbol: {symbol}")
        print(f"{Fore.GREEN}Decimals: {decimals}")
        print(f"{Fore.GREEN}Total Supply: {supply:,.0f}")
        print(f"\n{Fore.YELLOW}Full honeypot simulation coming in next version.")
        print(f"{Fore.YELLOW}For now, always check on honeypot.is or similar before buying.")
        
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        print("Token may not be a standard ERC-20")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="Token contract address")
    parser.add_argument("--chain", default="base", choices=list(CHAINS.keys()))
    args = parser.parse_args()
    check_token(args.token, args.chain)
