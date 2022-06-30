import binance
import time


def pair_split(pair):
    exchange_info = binance.Client().get_exchange_info()
    results = next(pair_ for pair_ in
                   exchange_info['symbols']
                   if pair_['symbol'] == pair)
    return [results['baseAsset'], results['quoteAsset']]


print(
    pair_split('LTCBTC')
)
