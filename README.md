## CEX arbitrage bot
CEX arbitrage bot is a simple CEX arbitrage bot that tracks price difference between multiple pairs in a CEX exchanges and calculates optimal trade size and profit.
It is mainly to show how to approach arbitrage opportunities on as well as a basic boiler-plate for CEX and DEX arbitrage algorithms.
## What is a CEX?

A Centralized exchange or CEX is operated in a centralized manner by a company. Orders on a CEX are maintained in an order book where buyers and sellers place their bids and a trade executes when the bids match.

## Features
- Multiple routes, and tokens
- Forward and Reverse Pair combination
- Dynamic Order-Book calculation
- High perfomance based flow and surface arbitrage calculation 
- Minimum and Maximum trade profit

[//]: # ()
[//]: # (## Install)

[//]: # ()
[//]: # (#### 1. Install Python  )

[//]: # (<code>npm install --save-dev hardhat</code>  )

[//]: # ()
[//]: # (#### 2. Create `.env` and set Alchemy API key to ALCHEMY_API_KEY)

[//]: # ()
[//]: # (#### 3. Set Ethereum address private key to PRIVATE_KEY in `.env`)

[//]: # ()
[//]: # (### Run)

[//]: # ()
[//]: # (Run mainnet fork node on localhost: `npx hardhat node --fork https://eth-mainnet.alchemyapi.io/v2/[API_KEY]`  )

[//]: # ()
[//]: # (Deploy contracts: `npx hardhat --network localhost run scripts/deploy.js`  )

[//]: # ()
[//]: # (Open console: `npx hardhat --network localhost console`  )

[//]: # ()
[//]: # (Run bot: `npx hardhat --network localhost run scripts/trade.js`  )
