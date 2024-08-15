import requests

def get_tickers():
    url = "https://api.kucoin.com/api/v1/market/allTickers"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']
    else:
        print("Error")

    pairs_prices = {}
    for i in data['ticker']:
        pair = i['symbol'].replace('-', '')
        price = 0.0 if i['last'] is None else float(i['last'])
        vol = float(i['volValue'])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity

    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  # len~1281 -> 805
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
