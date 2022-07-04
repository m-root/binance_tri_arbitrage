def order_book_orders(orders, qty):
    '''
    orders : list of all the trades in either ASKS or BIDS
    qty : Quantity passes to calculate
    :param orders:
    :param qty:
    :return:
    '''
    count = 0
    qty_sum = 0
    depth_sum = 0

    for depth in orders:
        if float(depth[1]) >= qty:
            depth_sum += (float(depth[0]) * qty)
            qty_sum += qty
            return depth_sum / qty_sum

        qty -= float(depth[1])
        if qty <= 0:
            break

        depth_sum += (float(depth[0]) * float(depth[1]))
        qty_sum += float(depth[1])
        count += 1

    return depth_sum / qty_sum



