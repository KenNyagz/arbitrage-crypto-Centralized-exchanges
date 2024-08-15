import requests

def get_tickers():
    url = "https://openapi.digifinex.com/v3/ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['ticker']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        if float(i['base_vol']) > 5000:
            pair = i['symbol'].replace('_', '')
            price = float(i['last'])
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) # 630 -> 493
    return pairs_prices

if __name__ == "__main__":
    get_tickers()