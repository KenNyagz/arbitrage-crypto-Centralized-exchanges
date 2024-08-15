import requests

def get_tickers():
    url = "https://www.bitmex.com/api/v1/instrument"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()

    pairs_prices = {}
    for i in data:
        pair = i['symbol']
        if not i.get('lastPrice'):
            continue
        price = float(i['lastPrice'])
        vol = float(i['volume24h'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity

    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  #len~ 1/94.sh*t exchange.
    
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
