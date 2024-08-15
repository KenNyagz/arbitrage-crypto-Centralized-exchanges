import requests

def get_tickers(okx_secret=None):
    # if okx_secret == None:
        # with open('api_secret', 'r') as f:
           # secret = f.read()
    #else:
        #secret = okx_secret
    #public_key = '6114f3f9-1c11-47b4-ba6a-7bf5dca15972'    

    url = 'https://whitebit.com/api/v1/public/tickers'
    response = requests.get(url)
    data = response.json()['result']

    pairs_prices = {}
    for i in data:
        pair = i
        pair = pair.replace('_', '') # remove dash separating coins in pair
        price = float(data[i]['ticker']['last'])
        vol = float(data[i]['ticker']['deal'])
        if vol > 5000:
            pairs_prices.update({pair: price})

    #for pair in pairs_prices:
    #    print(pair, ':', pairs_prices[pair]) # visualisation
    #print(len(pairs_prices)) #~ 501 -> 403
    return pairs_prices


if __name__ == "__main__":
    get_tickers()
