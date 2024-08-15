import requests

def get_tickers():
    url = " https://sapi.xt.com/v4/public/ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['result']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        pair = i['s'].replace('_', '')
        price = float(i['c'])
        vol = float(i['v'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  #len~1386 -> 1082
    return pairs_prices

if __name__ == "__main__":
    get_tickers()