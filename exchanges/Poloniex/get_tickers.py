import requests

def get_tickers():
    url = "https://api.poloniex.com/markets/ticker24h"
    #url = 'https://poloniex.com/public?command=returnTicker' # this might be the API endpoint that includes vol data
                                                              # But it doesn't work for some reason, try again later
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        print("Error")

    pairs_prices = {}
    for i in data:
        if float(i['amount']) > 5000:
            pair = i['displayName'].replace('/', '')
            price = (float(i['ask']) + float(i['bid'])) / 2
            pairs_prices.update({pair.upper(): price}) #Uppercase for uniformity
    
    #for pair in pairs_prices:
    #    print(pair + " : " + str(pairs_prices[pair]))  # len~990 -> 121
    return pairs_prices

if __name__ == "__main__":
    get_tickers()
