import requests

def get_tickers(okx_secret=None):
    url = 'https://api.bitget.com/api/spot/v1/market/tickers'
    response = requests.get(url)
    data = response.json()['data']

    pairs_prices = {}
    for i in data:
        if float(i['usdtVol']) > 5000:   # Bitget makes life very easy here by 
            pair = i['symbol']           # giving a 'usdtVol' value. A relief from the conversion logic needed
            price = i['close']
            pairs_prices.update({pair: float(price)})
       
    #for pair in pairs_prices:
    #    print(pair, ':', pairs_prices[pair]) # visualisation len~=958 -> 873
    return pairs_prices


if __name__ == "__main__":
    get_tickers()
