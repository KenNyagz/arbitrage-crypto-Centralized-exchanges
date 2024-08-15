import requests

def get_tickers():
    prices_url = 'https://open-api.bingx.com/openApi/swap/v2/quote/ticker'
               
    resp = requests.get(prices_url).json()
    pairs = resp['data']
    pairs_prices = {}

    for i in pairs:
        pair = i['symbol'].replace('-', '')
        price = float(i['lastPrice'])
        vol = float(i['quoteVolume'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) # len~266/266
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
