import binance


def orderbook_tickers():
    client = binance.Client()
    tickers = client.get_orderbook_tickers()
    return tickers


def exchange_info():
    client = binance.Client()
    info = client.get_exchange_info()
    return info['symbols']


def pair_ask_bid(orderbook_tickers, pair):
    '''
    {
    'symbol': 'OPEUR',
    'bidPrice': '0.56100000',
    'bidQty': '594.97000000',
    'askPrice': '0.57300000',
    'askQty': '593.10000000'
    }
    :param pair:
    :return:
    '''
    results = next(pair_ for pair_ in orderbook_tickers if pair_['symbol'] == pair)
    return results

def pair_depth(symbol):
    #todo
    binance.Client().get_order_book(symbol=symbol)['asks']
    binance.Client().get_order_book(symbol=symbol)['bids']


def pair_split(info, pair):
    results = next(pair_ for pair_ in
                   info if pair_['symbol'] == pair)
    return [results['baseAsset'], results['quoteAsset']]
