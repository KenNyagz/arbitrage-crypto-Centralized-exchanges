import requests

def get_tickers():
    url = "https://api.huobi.pro/market/tickers"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        if float(i['vol']) > 5000:
            pair = i['symbol']
            price = (float(i['ask']) + float(i['bid'])) / 2 # Avg of bid and ask since no 'last'
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) # ~807 -> 689
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
