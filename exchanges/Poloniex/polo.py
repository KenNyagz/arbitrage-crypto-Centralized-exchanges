# import this package
from poloniex import Poloniex
# https://github.com/s4w3d0ff/python-poloniex
# make an instance of poloniex.Poloniex
polo = Poloniex()
help(polo)

polo.returnTicker()
print(polo('returnTicker'))