import requests

def get_tickers():
    url = "https://api.mexc.com/api/v3/ticker/24hr"
    headers = {
        'X-MEXC-APIKEY': '',
        'Content-Type':	'application/json'
    }

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        pair = i['symbol']
        price = float(i['lastPrice'])
        vol = 0.0 if i['quoteVolume'] is None else float(i['quoteVolume'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  # len~2915 -> ~2150
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
