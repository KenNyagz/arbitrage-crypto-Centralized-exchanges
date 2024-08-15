import krakenex
from pykrakenapi import KrakenAPI
#help(KrakenAPI)
api = krakenex.API()
k = KrakenAPI(api)
ticker_data = api.query_public('Ticker')
print(ticker_data)