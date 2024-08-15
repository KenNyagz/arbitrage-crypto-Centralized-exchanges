import requests

def get_tickers(okx_secret=None):
    url = 'https://api.bybit.com/v5/market/tickers?category=spot'
    response = requests.get(url)
    data = response.json()['result']['list']

    pairs_prices = {}
    #for i in data['result']['list']:
    for i in data:
        if float(i['turnover24h']) > 5000:
            pair = i['symbol']
            price = i['lastPrice']
            pairs_prices[pair] = float(price)
    
    #for pair in pairs_prices:
    #    print(pair, ':', pairs_prices[pair]) # visualisation len 537/587
    return pairs_prices


if __name__ == "__main__":
    get_tickers()
