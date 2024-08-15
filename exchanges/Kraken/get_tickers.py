import requests

def get_tickers():
    # https://algotrading101.com/learn/kraken-api-guide/  - Handy Kraken api guide

    url = "https://api.kraken.com/0/public/Ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['result']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        vol = float(data[i]['v'][1])  # Volume written as base currency
        pair = i
        price = float(data[i]['c'][0])
        if vol * price > 5000:   # Checking volume after converting it to quote currency as USDT is quote currency in many pairs
            pairs_prices.update({pair.upper(): price}) # Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) #Viz *len~809 -> 437 after slash
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
