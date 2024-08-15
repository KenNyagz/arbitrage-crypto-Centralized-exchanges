import requests

def get_tickers():
    url = "http://ascendex.com/api/pro/v1/spot/ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        pair = i['symbol'].replace('/', '')
        price = (float(i['ask'][0]) + float(i['bid'][0])) / 2 # Avg of bid & ask orice since they are not offering latest price
        vol = float(i['volume']) # volume offered only in base currency
        if vol * price > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  #len~489 / 438 after vol filter
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
