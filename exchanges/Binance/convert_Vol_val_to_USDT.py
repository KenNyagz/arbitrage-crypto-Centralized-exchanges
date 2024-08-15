import requests
import sys
# Base URL for the Binance API
base_url = "https://api.binance.com"

# Get the 24hr ticker price change statistics
ticker_24hr = requests.get(f"{base_url}/api/v3/ticker/24hr").json()

# Get the latest prices
prices = requests.get(f"{base_url}/api/v3/ticker/price").json()

price_dict = {item['symbol']: float(item['price']) for item in prices}

usdt_volumes = {}

for ticker in ticker_24hr:
    symbol = ticker['symbol']
    quote_volume = float(ticker['quoteVolume'])

    if symbol.endswith("USDT"):
        # Directly use the quoteVolume as it's already in USDT
        usdt_volume = quote_volume
    else:
        # Extract the quote currency
        base, quote = symbol[:-3], symbol[-3:]
        if quote == "BTC":
            usdt_volume = quote_volume * price_dict["BTCUSDT"]
        elif quote == "ETH":
            usdt_volume = quote_volume * price_dict["ETHUSDT"]
        else:
            continue  # Add more pairs if necessary

    usdt_volumes[symbol] = usdt_volume

# Print the USDT volume for each pair
for symbol, usdt_volume in usdt_volumes.items():
    print(f"{symbol}: {usdt_volume} USDT")

