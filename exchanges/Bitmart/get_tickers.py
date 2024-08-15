import requests

def get_tickers():
    url = "https://api-cloud.bitmart.com/spot/quotation/v3/tickers"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()['data']

    pairs_prices = {}
    for i in data:
        pair = i[0].replace('_', '')
        price = float(i[1])
        vol = float(i[3])
        if vol > 5000:
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  #len~ 974 / 1154  after vol filter #len ~ 1207 / 1013
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
