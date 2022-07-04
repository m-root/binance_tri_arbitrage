def pair_sorting(starting_asset, pair_collection):
    '''
    starting asset for an array of pairs to sort out
    and arrange before any trade execution while using
    'closed chain link' algo. Examples on the code below.

    https://gist.github.com/m-root/ed47e17336pair_ee8bd9eddf7060epair_e2b

    :param starting_asset:
    :param pair_collection:
    :return: pair collection
    '''
    pairs = []
    while len(pair_collection) > 0:
        for pair_ in pair_collection:
            if starting_asset not in pair_:
                pair_ = [pair for pair in pair_collection if starting_asset in pair][0]
            ans = separator(starting_asset, pair_)
            pair_collection.remove(pair_)
            starting_asset = ans
            pairs.append(pair_)
    return pairs


def separator(asset, pair):
    '''
    Separator for assets in a pair
    :param asset:
    :param pair:
    :return: asset in various position
    '''
    if pair.index(asset) == 0:
        return pair[1]
    else:
        return pair[0]
