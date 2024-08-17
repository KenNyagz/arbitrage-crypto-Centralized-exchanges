#!/usr/bin/python3
from datetime import datetime
from itertools import combinations
from exchanges.Binance.get_tickers import get_tickers as binance_tickers_
from exchanges.Huobi.get_tickers import get_tickers as huobi_tickers_
from exchanges.OKX.get_tickers import get_tickers as okx_tickers_
from exchanges.GateIO.get_tickers import get_tickers as gateio_tickers_
from exchanges.Bybit.get_tickers import get_tickers as bybit_tickers_
from exchanges.BingX.get_tickers import get_tickers as bingx_tickers_
from exchanges.Bitget.get_tickers import get_tickers as bitget_tickers_
from exchanges.Bitrue.get_tickers import get_tickers as bitrue_tickers_
from exchanges.Kraken.get_tickers import get_tickers as kraken_tickers_
from exchanges.KuCoin.get_tickers import get_tickers as kucoin_tickers_
from exchanges.Mexc.get_tickers import get_tickers as mexc_tickers_
from exchanges.Poloniex.get_tickers import get_tickers as poloniex_tickers_
from exchanges.XT.get_tickers import get_tickers as xt_tickers_
from exchanges.AscendEx.get_tickers import get_tickers as ascendex_tickers
from exchanges.Bitmart.get_tickers import get_tickers as bitmart_tickers
from exchanges.CoinEx.get_tickers import get_tickers as coinex_tickers
from exchanges.Digifinex.get_tickers import get_tickers as digifinex_tickers
from exchanges.Hotcoin.get_tickers import get_tickers as hotcoin_tickers
from exchanges.LBank.get_tickers import get_tickers as lbank_tickers
from exchanges.Probit.get_tickers import get_tickers as probit_tickers
from exchanges.Whitebit.get_tickers import get_tickers as whitebit_tickers

def get_secret(file_name):
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")
    with open(file_name, 'r') as f:
        exchange_secret = f.read()
    return exchange_secret

# getting the secret keys
#binance_secret = get_secret("Binance/api_secret") # Not in use for now
#okx_secret = get_secret("OKX/api_secret") # Not in use at the moment

# Getting all ticker symbols and their prices from exchanges
binance_tickers = binance_tickers_()
huobi_tickers = huobi_tickers_() #
okx_tickers = okx_tickers_()
gateio_tickers = gateio_tickers_("test") #
bybit_tickers = bybit_tickers_('tst')
bingx_tickers = bingx_tickers_()
bitget_tickers = bitget_tickers_()
bitrue_tickers = bitrue_tickers_()
kraken_tickers = kraken_tickers_()
kucoin_tickers = kucoin_tickers_()
mexc_tickers = mexc_tickers_()
poloniex_tickers = poloniex_tickers_()
xt_tickers = xt_tickers_()
ascendex_tickers = ascendex_tickers()
bitmart_tickers = bitmart_tickers()
coinex_tickers = coinex_tickers()
digifinex_tickers = digifinex_tickers()
hotcoin_tickers = hotcoin_tickers()
lbank_tickers = lbank_tickers()
probit_tickers = probit_tickers()
whitebit_tickers = whitebit_tickers()


def get_arbtg(exchange1, exchange2, exchange1_tickers, exchange2_tickers):
    common_tickers = {}
    for ticker in exchange1_tickers:
        if ticker in exchange2_tickers:
            common_tickers[ticker] = exchange1_tickers[ticker]

    result = f"Common tickers in {exchange1} and {exchange2} are: {len(common_tickers)}\n"

    percentage_diffs = {f"percentage_to_{exchange1}": 0.0, f"percentage_to_{exchange2}": 0.0}
    for ticker in common_tickers:
        if exchange1_tickers[ticker] > exchange2_tickers[ticker]:
            difference = exchange1_tickers[ticker] - exchange2_tickers[ticker]

            try:
                percentage_diffs[f"percentage_to_{exchange1}"] = difference / exchange1_tickers[ticker] * 100
                percentage_diffs[f"percentage_to_{exchange2}"] = (difference / exchange2_tickers[ticker]) * 100
            except ZeroDivisionError as e:
                 #print(f"zeroDivERROR:{ticker} : {exchange1_tickers[ticker]} ~ {exchange2_tickers[ticker]}")
                 continue

            if percentage_diffs[f"percentage_to_{exchange1}"] > 3:
                #print(ticker, end=" : ")
                # #print(percentage_diffs[f"percentage_to_{exchange1}"], f"% favouring {exchange2}") ## Don't uncomment unless testing
                #print(percentage_diffs[f"percentage_to_{exchange2}"], f"% favouring {exchange1}")
                # #result += f"{ticker} : difference is {percentage_diffs[f'percentage_to_{exchange1}']}% favouring {exchange2}\n" ## Don't uncomment unless testing
                result += f"{ticker} : difference is {percentage_diffs[f'percentage_to_{exchange2}']}% favouring {exchange1}\n" # return value construct

        elif exchange2_tickers[ticker] > exchange1_tickers[ticker]:
            difference = exchange2_tickers[ticker] - exchange1_tickers[ticker]
            try:
                percentage_diffs[f"percentage_to_{exchange2}"] = difference / exchange2_tickers[ticker] * 100
                percentage_diffs[f"percentage_to_{exchange1}"] = (difference / exchange1_tickers[ticker]) * 100
            except ZeroDivisionError as e:
                 #print(f"zeroDivERROR:{ticker} : {exchange1_tickers[ticker]} ~ {exchange2_tickers[ticker]}")
                 continue

            if percentage_diffs[f"percentage_to_{exchange2}"] > 3:
                #print(ticker, end=" : ")
                # #print(percentage_diffs[f"percentage_to_{exchange2}"], f"% favouring {exchange1}") ## Don't uncomment unless testing
                #print(percentage_diffs[f"percentage_to_{exchange1}"], f"% favouring {exchange2}")
                # #result += f"{ticker} : difference is {percentage_diffs[f'percentage_to_{exchange2}']}% favouring {exchange1}\n" ## Don't uncomment unless testing
                result += f"{ticker} : difference is {percentage_diffs[f'percentage_to_{exchange1}']}% favouring {exchange2}\n" #Constructing return value

    if result.count('\n') <= 1:
        result += '  --  No arbitrage above 3% --\n'
    return result


def display_arbitrage_opportunities(exchange1, exchange2, exchange1_tickers, exchange2_tickers, timestamp):
    '''Displays percentage price diffs btn two exchanges'''
    with open(f'ticker_arbs/{timestamp}', 'a') as f:   # for storing arbitrage data in files, for persistence and future ref
        print(exchange1,'and', exchange2, ' \n ', get_arbtg(exchange1, exchange2, exchange1_tickers, exchange2_tickers), file=f)
        ##  result = subprocess.run(['python3', 'arbitrage.py'], stdout=f, stderr=subprocess.STDOUT)

    print('\n', exchange1,'and', exchange2, ' \n ', get_arbtg(exchange1, exchange2, exchange1_tickers, exchange2_tickers)) # To stdout for display


def main():
    ''' program entry point'''
    tickers = [ binance_tickers, huobi_tickers, okx_tickers, gateio_tickers, bingx_tickers,
                bybit_tickers, bitget_tickers, bitrue_tickers, kraken_tickers, kucoin_tickers,
                mexc_tickers, poloniex_tickers, xt_tickers, ascendex_tickers, bitmart_tickers, coinex_tickers,
                digifinex_tickers, hotcoin_tickers, lbank_tickers, probit_tickers, whitebit_tickers,
              ]
    exchanges = ['Binance', 'Huobi', 'OKX', 'GateIO', 'BingX', 'Bybit', 'Bitget', 'Bitrue', 'Kraken', 'Kucoin', 'Mexc',
                 'Poloniex', 'XT', 'AscendEX', 'Bitmart', 'CoinEx', 'Digifinex', 'Hotcoin', 'Lbank', 'Probit', 'Whitebit'
                ]

    now = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')  # for precise file creation, storage files are named from timestamp
    exchange_combinations = combinations(zip(exchanges, tickers), 2)
    for (exchange1, tickers1), (exchange2, tickers2) in exchange_combinations:
        display_arbitrage_opportunities(exchange1, exchange2, tickers1, tickers2, now)

if __name__ == '__main__':
    main()