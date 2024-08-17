# ARBITRAGE COVE

The project aims to seek as many possible and legitimate arbitrage opportunities between centralized crytocurrency exchanges.

It collects data from various cryptocurrency exchanges via their API endpoints, processes and filters that data then stores the resulting symbols and their prices. It then proceeds to compare the price data two exchanges at a time. For the symbols that are common between the two exchanges being compared, the price difference is compared as a percentage. If it's above a certain threshold(3%) it is saved as a potential arbitrage opportunity. All potential arbitrage opportunities are then printed out.

### Set up
`pip install -r requiremnts.txt`

### API
#### Base Url


#### API endpoints:
`[GET] /home` : Serves the home/landing page

`[GET] /arbitrage` : Retrieves the arbitrage opportunities between various centralized exchanges
