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

    TriangularPairList = []
    RemoveDuplicatesList = []

    '''
    Create a list of all pairs
    Loop through to get the first pair combination without any matching pairs
    Loop through to get the second pair combination without any matching pairs
    '''

    for pair_a in pairList:
        a_baseAsset = pair_a['baseAsset']
        a_quoteAsset = pair_a['quoteAsset']
        first_pair_split = [a_baseAsset, a_quoteAsset]

        for pair_b in pairList:
            b_baseAsset = pair_b['baseAsset']
            b_quoteAsset = pair_b['quoteAsset']

            if pair_a != pair_b:
                if b_baseAsset in first_pair_split or b_quoteAsset in first_pair_split:
                    add = [b_baseAsset, b_quoteAsset]
                    second_pair_split = first_pair_split + add

                    for pair_c in pairList:
                        c_baseAsset = pair_c['baseAsset']
                        c_quoteAsset = pair_c['quoteAsset']
                        if pair_a != pair_b and pair_b != pair_c and pair_c != pair_a:
                            if a_baseAsset in second_pair_split or a_quoteAsset in second_pair_split:
                                add = [c_baseAsset, c_quoteAsset]
                                third_pair_split = second_pair_split + add
                                numpy.array(third_pair_split)
                                unique, counts = numpy.unique(third_pair_split, return_counts=True)
                                if len(unique) ==3:
                                    print(third_pair_split)
                                    TriangularPairList.append([pair_a['symbol'], pair_b['symbol'], pair_c['symbol']])

                                    '''
                                    create a new array = unique_sort
                                    check unique and put it in an array
                                    unique_sort = unique_sort + unique
                                    if unique is not in unique_sort
                                        TriangularPairList.append()
                                    
                                    a_baseAsset 
                                    a_quoteAsset
                                    b_baseAsset 
                                    b_quoteAsset
                                    c_baseAsset 
                                    c_quoteAsset
                                    pair_a
                                    pair_b
                                    pair_c
                                    pairs
                                    
                                    Dumping to Json
                                    '''

    print(len(TriangularPairList))




getPairs()
