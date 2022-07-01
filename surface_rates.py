import pair_funct

'''
load json file
pull prices
ws subscription: All Market Mini Tickers Stream
'''


# Structure Prices for tokens
def get_coin_token_prices():
    pass


def collect_tradable_pairs():
    pass


def structure_triangular_pairs():
    pass


def get_pair_prices():
    """
    Extract Pair info
    """


'''
Calculate Surface Rate Arbitrage Opportunity

Ask = 19094
BTC-USDT
Bid = 19090

'''


def flow_calc(start_asset, quantity, pair_, bid_price, ask_price):
    ''' direction_trade_1 = "base => quote"'''
    if pair_funct.pair_split(pair_)[0] == start_asset:
        swap = quantity * bid_price
        return swap

    # Starting with quote and trading for a base
    elif pair_funct.pair_split(pair_)[1] == start_asset:
        ''' direction_trade_1 = "base <= quote"'''
        swap = quantity / ask_price
        return swap


def calc_tri_arb_surf_rate():
    """
    Extract Pair info
    ['ETH', 'BTC', 'BTC', 'DASH', 'ETH', 'DASH']
    ['ETH', 'BTC', 'DASH','BTC',  'ETH', 'DASH']
    ['ETH', 'BTC', 'DASH', 'ETH', 'BTC',  'DASH']
    ['ETH', 'BTC', 'DASH', 'ETH', 'DASH', 'BTC']
    ['BTC', 'ETH', 'DASH', 'ETH', 'DASH', 'BTC']
    ['ETH', 'DASH', 'BTC', 'ETH', 'DASH', 'BTC']
    """
    starting_qty = 1
    min_surface_rate = 0
    surface_dict = {}
    contract_2 = ""
    contract_3 = ""
    direction_trade_1 = ""
    direction_trade_2 = ""
    direction_trade_3 = ""
    acquired_coin_t2 = 0
    acquired_coin_t3 = 0
    calculated = 0

    '''
    Get Pair Variable
    '''
    a_base = ''
    a_quote = ''
    b_base = ''
    b_quote = ''
    c_base = ''
    c_quote = ''
    pair_a = ''
    pair_b = ''
    pair_c = ''
    start_asset = 'BUSD'

    '''
    Get Prices
    
    {
    'symbol': 'OPEUR',
    'bidPrice': '0.56100000',
    'bidQty': '594.97000000',
    'askPrice': '0.57300000',
    'askQty': '593.10000000'
    }
    '''
    pair_a_data = pair_funct.pair_ask_bid(pair=pair_a)
    pair_b_data = pair_funct.pair_ask_bid(pair=pair_b)
    pair_c_data = pair_funct.pair_ask_bid(pair=pair_c)

    # a_ask_price = float(pair_a_data['askPrice'])
    # a_ask_qty = float(pair_a_data['askQty'])
    # a_bid_price = float(pair_a_data['bidPrice'])
    # a_bid_qty = float(pair_a_data['bidQty'])
    # b_ask_price = float(pair_b_data['askPrice'])
    # b_ask_qty = float(pair_b_data['askQty'])
    # b_bid_price = float(pair_b_data['bidPrice'])
    # b_bid_qty = float(pair_b_data['bidQty'])
    # c_ask_price = float(pair_c_data['askPrice'])
    # c_ask_qty = float(pair_c_data['askQty'])
    # c_bid_price = float(pair_c_data['bidPrice'])
    # c_bid_qty = float(pair_c_data['bidQty'])
    #
    # direction_ = ['forward', 'reverse']

    # ['ETHDASH', 'BTCETH', 'DASHBTC']
    pair_list = []
    for pair in pair_list:
        pair_data = pair_funct.pair_ask_bid(pair=pair)
        ask_price = float(pair_data['askPrice'])
        if pair_list.index(pair) == 0:
            quantity = float(pair_data['askQty'])
        bid_price = float(pair_data['bidPrice'])
        quantity = flow_calc(start_asset, quantity, pair, bid_price, ask_price)

    '''
    Binance Swaps Rule of the thumb
    ---------------------------------------
    From Left to Right => quantity*bidPrice
    From Right to Left => quantity/askPrice
    3
    2
    '''

    swap_1 = 0
    swap_2 = 0
    swap_3 = 0
    swap_rate_1 = 0
    swap_rate_2 = 0
    swap_rate_3 = 0

    # Starting with base and trading for a quote
    '''
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
    '''
    ######################################################
    ######################################################
    ######################################################
    ######################################################
    ######################################################
    ######################################################
    ######################################################
    '''
    Check start_asset index
    if start_asset index 01
    
    '''
    # contract_1 = pair_a
    # acquired_coin_t1 = starting_qty


'''Reformat Order Book for Depth Calculation'''


def order_book_price_format():
    pass


# Get Acquired Coin Also Known As Depth Calculation
def calculate_acquired_coin(amount_in, orderbook):
    """
        CHALLENGES
        Full amount of starting amount can be eaten on the first level (level 0)
        Some of the amount in can be eaten up by multiple levels
        Some coins may not have enough liquidity
    """


# Get the Depth From the Order Book
def get_depth_from_orderbook(surface_arb):
    pass
    # Extract initial variables
