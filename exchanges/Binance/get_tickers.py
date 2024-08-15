import requests

def get_tickers():

    url = 'https://api.binance.com/api/v3/ticker/24hr'
    response = requests.get(url)
    data = response.json()

    pairs_prices = {}
    for i in data:
        if float(i['quoteVolume']) > 5000: # Intended to filter low volume pairs, but as it is
            pair = i['symbol']             # it also filters high value pairs that are even more legitimate eg BTCETH
            price = i['lastPrice']         # Will better it later. Consult "convert_Vol_val_to_USDT.py" in same dir
            pairs_prices.update({pair: float(price)})
    
    #for pair in pairs_prices:
    #    print(pair, ':', pairs_prices[pair]) # visualisation len 871/2703
    return pairs_prices


if __name__ == "__main__":
    get_tickers()
