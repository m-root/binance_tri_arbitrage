import time

from payload import pair_funct

'''
load json file
pull prices
ws subscription: All Market Mini Tickers Stream
'''
info = pair_funct.exchange_info()


def flow_calc(start_asset, quantity, pair_, bid_price, ask_price):
    '''
    Binance Swaps Rule of the thumb
    -------------------------------------------
    From Left to Right => quantity*bidPrice
    From Right to Left => quantity/askPrice
    ---------------------------------------------
    Calculate Surface Rate Arbitrage Opportunity
    ---------------------------------------------
    '''
    print(start_asset, quantity, pair_, bid_price, ask_price)

    if pair_funct.pair_split(info, pair_)[0] == start_asset:
        swap = quantity * bid_price
        return [swap, pair_funct.pair_split(info, pair_)[1]]

    # Starting with quote and trading for a base
    elif pair_funct.pair_split(info, pair_)[1] == start_asset:
        ''' direction_trade_1 = "base <= quote"'''
        swap = quantity / ask_price
        return [swap, pair_funct.pair_split(info, pair_)[0]]


def calc_arb_surf_rate():
    """
    Extract Pair info
    First pair then break it down to base and quote
    Trade_01
    Pair = [a,b]
    Tri_pair = [ab, cb, ac]
    Quad = [ab,bc,cd, da]
    5x = [ab,bc, cd,de, ea]
    Asset = a/ b
    If starting_asset = a

    Level 1
    If a trade a for b
    If b trade b for a

    Level 2

    """
    starting_qty = 1
    start_asset = 'USDT'

    pair_list = ['ETHUSDT', 'ETHBTC', 'BTCBUSD', 'BUSDUSDT']
    orderbook_tickers = pair_funct.orderbook_tickers()

    for pair in pair_list:
        # if pair not in pair_list todo
        print(pair)
        pair_data = pair_funct.pair_ask_bid(orderbook_tickers, pair=pair)
        ask_price = float(pair_data['askPrice'])
        if pair_list.index(pair) == 0:
            quantity = starting_qty
        bid_price = float(pair_data['bidPrice'])
        print(bid_price)
        qty = flow_calc(start_asset, quantity, pair, bid_price, ask_price)
        quantity = qty[0]
        start_asset = qty[1]

        print(f'Quantity is : {quantity}')

c = time.time()
print(calc_arb_surf_rate())
print(time.time()-c)
