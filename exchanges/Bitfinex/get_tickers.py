import requests
# Bitfinex is a bit of a weird exchange, unconventional pairs, symbols and stablecoins

def get_tickers():
    url = "https://api-pub.bitfinex.com/v2/tickers?symbols=ALL"
    # https://docs.bitfinex.com/reference/rest-public-tickers - API guide on how they've weirdly organised their data

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        print("Error")
    '''
    exchange = ccxt.bitfinex()
    tickers = exchange.fetch_tickers()
    print(tickers)
    ''' 
    pairs_prices = {}
    for i in data:
        pair = i[0]
        price = i[7] # Avg of bid & ask orice since they are not offering latest price
        vol = i[8] # volume offered only in base currency
        if vol * price > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) #len 256/507
    return pairs_prices

if __name__ == "__main__":
    get_tickers()