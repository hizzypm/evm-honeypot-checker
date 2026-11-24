# EVM Honeypot / Token Safety Checker

Open-source Python tool to scan ERC-20 tokens for honeypot, high taxes, and other risks before you buy.

## Features
- Checks if token is a honeypot (can buy but not sell)
- Estimates buy/sell tax
- Checks owner privileges, liquidity locks
- Multi-chain support (ETH, Base, Arbitrum, BSC, etc.)
- Simple CLI

## Installation
```bash
git clone https://github.com/hizzypm/evm-honeypot-checker.git
cd evm-honeypot-checker
pip install -r requirements.txt
```

## Usage
```bash
python check_token.py 0xTOKEN_ADDRESS --chain base
```

Always DYOR. This is not financial advice.
