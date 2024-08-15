import requests

def get_tickers():
    url = "https://api.coinex.com/v1/market/ticker/all"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
    else:
        print("Error")

    pairs_prices = {}
    for ticker, details in data['ticker'].items():
        pair = ticker
        price = float(details['last'])
        vol = float(details['vol'])
        if vol * price > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  # len~1478 -> 708
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
