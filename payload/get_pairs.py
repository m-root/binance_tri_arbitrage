import json
import numpy
import binance

"""
get all pairs and their splits for base and quote
https://api.binance.com/api/v3/exchangeInfo
create an array to get triangular pairs
create an array to get and remove duplicates
get pair A, Get Pair B, Get Pair C
"""


def exchangeInfo():
    exch_info = binance.Client().get_exchange_info()
    return exch_info['symbols']


def getPairs():
    pairList = []
    for pairs in exchangeInfo():
        if pairs['isSpotTradingAllowed'] == True and pairs['status'] == 'TRADING':
            pairList.append(pairs)
            # print(pairList)

    tri_pairs_data = []
    key_token = []

    '''
    Create a list of all pairs
    Loop through to get the first pair combination without any matching pairs
    Loop through to get the second pair combination without any matching pairs
    '''

    for pair_a in pairList:
        a_baseAsset = pair_a['baseAsset']
        a_quoteAsset = pair_a['quoteAsset']
        first_pair_split = [a_baseAsset, a_quoteAsset]
        _tokens = []
        _tokens.append(a_baseAsset)
        _tokens.append(a_quoteAsset)

        for pair_b in pairList:
            b_baseAsset = pair_b['baseAsset']
            b_quoteAsset = pair_b['quoteAsset']

            if pair_a != pair_b:
                if b_baseAsset in first_pair_split or b_quoteAsset in first_pair_split:
                    add = [b_baseAsset, b_quoteAsset]
                    second_pair_split = first_pair_split + add
                    if b_baseAsset not in _tokens:
                        _tokens.append(b_baseAsset)
                    else:
                        _tokens.append(b_quoteAsset)

                    for pair_c in pairList:
                        c_baseAsset = pair_c['baseAsset']
                        c_quoteAsset = pair_c['quoteAsset']

                        if pair_a != pair_b and pair_b != pair_c and pair_c != pair_a and _tokens not in key_token:
                            if a_baseAsset in second_pair_split or a_quoteAsset in second_pair_split:
                                key_token.append(_tokens)
                                add = [c_baseAsset, c_quoteAsset]
                                third_pair_split = second_pair_split + add
                                numpy.array(third_pair_split)
                                unique, counts = numpy.unique(third_pair_split, return_counts=True)
                                if len(unique) == 3:
                                    print(third_pair_split)

                                    data = {
                                        'a_baseAsset': a_baseAsset,
                                        'a_quoteAsset': a_quoteAsset,
                                        'b_baseAsset': b_baseAsset,
                                        'b_quoteAsset': b_quoteAsset,
                                        'c_baseAsset': c_baseAsset,
                                        'c_quoteAsset': c_quoteAsset,
                                        'pair_a': pair_a['symbol'],
                                        'pair_b': pair_b['symbol'],
                                        'pair_c': pair_c['symbol'],
                                        'pairs': [pair_a['symbol'], pair_b['symbol'], pair_c['symbol']]
                                    }

                                    tri_pairs_data.append(data)

    with open('tri_arbitrage_pairs.json', 'w') as f:
        json.dump({'tri_arbitrage_pairs': tri_pairs_data}, f)
    return {'tri_arbitrage_pairs': tri_pairs_data}

