import requests

def get_tickers():
    url = " https://api.probit.com/api/exchange/v1/ticker"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        if float(i['quote_volume']) > 10000:
            pair = i['market_id'].replace('-', '')
            price = 0.0 if i['last'] == None else float(i['last'])
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair])) # ~864 -> 157
    return pairs_prices

if __name__ == "__main__":
    get_tickers()