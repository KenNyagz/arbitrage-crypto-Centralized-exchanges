import requests

def get_tickers():
    url = "https://api.lbkex.com/v1/ticker.do?symbol=all"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        pair = i['symbol'].replace('_', '')
        price = float(i['ticker']['latest'])
        vol = float(i['ticker']['turnover'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  # len~ 1194 -> 1033
    return pairs_prices

if __name__ == "__main__":
    get_tickers()