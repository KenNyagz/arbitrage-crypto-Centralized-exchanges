import requests

def get_tickers():
    url = "https://api.hotcoinfin.com/v1/market/ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['ticker']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        pair = i['symbol'].replace('_', '')
        price = float(i['last'])
        vol = float(i['vol'])
        if vol * price > 5000:  # Converting volume to base currency which is many times USDT
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity

    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))
    #print(len(pairs_prices)) # ~ 544 -> 501
    return pairs_prices

if __name__ == "__main__":
    get_tickers()