# arr = [[6, 1], [1, 2], [3, 4], [5, 6], [2, 3], [4, 5]]
# '''
# start_item = 1 or a and pair is b
# array with start item = last_item
# pair_part of start_item = b
# '''
#
# def separator(ab, b):
#     if b.index(ab) == 0:
#         return b[1]
#     else:
#         return b[0]
# import time
#
# def pair_sorting(start_item = 1, array_edit = arr):
#     new_arr = []
#     time_start = time.time()
#     print(time_start)
#     while len(array_edit) > 0:
#         for aa in array_edit:
#             if start_item not in aa:
#                 aa = [b for b in array_edit if start_item in b][0]
#                 print(aa)
#             ans = separator(start_item, aa)
#             print(ans)
#             array_edit.remove(aa)
#             start_item = ans
#             new_arr.append(aa)
#     print(time.time()-time_start)
#     print(new_arr)
#     return new_arr
#
# pair_sorting()
import time

import binance

# for d in binance.Client().get_order_book(symbol='BTCUSDT')['asks']:
#     print(d)


# print(c)

'''
num = 10
while (num >= 0):
    num -= 1
    print(num)
    
'''
import time

a = [['19115.22000000', '3.99830000'], ['19115.23000000', '0.00073000'], ['19115.27000000', '0.56735000'],
     ['19115.35000000', '0.02196000'], ['19115.38000000', '0.28291000'], ['19115.62000000', '0.06342000'],
     ['19115.63000000', '0.62700000'], ['19115.65000000', '0.10778000'], ['19115.70000000', '0.18231000'],
     ['19115.80000000', '0.01572000'], ['19116.02000000', '0.01000000'], ['19116.07000000', '0.00100000'],
     ['19116.08000000', '0.00054000'], ['19116.16000000', '0.04969000'], ['19116.22000000', '0.00103000'],
     ['19116.30000000', '0.00100000'], ['19116.46000000', '0.01250000'], ['19116.60000000', '0.27638000'],
     ['19116.72000000', '0.10246000'], ['19116.83000000', '0.13254000'], ['19117.02000000', '0.01000000'],
     ['19117.07000000', '0.00100000'], ['19117.12000000', '0.05164000'], ['19117.14000000', '0.24000000'],
     ['19117.47000000', '0.00059000'], ['19117.62000000', '0.11070000'], ['19117.66000000', '0.01572000'],
     ['19117.96000000', '0.07500000'], ['19118.02000000', '0.33000000'], ['19118.07000000', '0.00100000'],
     ['19118.22000000', '0.04000000'], ['19118.28000000', '0.43653000'], ['19118.35000000', '0.50690000'],
     ['19118.36000000', '0.12486000'], ['19118.41000000', '0.16000000'], ['19118.60000000', '0.08000000'],
     ['19118.95000000', '0.40328000'], ['19119.02000000', '0.01000000'], ['19119.05000000', '0.10000000'],
     ['19119.07000000', '0.00100000'], ['19119.26000000', '0.05564000'], ['19119.30000000', '0.00100000'],
     ['19119.37000000', '0.50000000'], ['19119.38000000', '0.10000000'], ['19119.70000000', '0.39986000'],
     ['19119.78000000', '0.01572000'], ['19119.85000000', '0.00825000'], ['19119.86000000', '0.00059000'],
     ['19120.00000000', '0.04947000'], ['19120.02000000', '0.01000000'], ['19120.07000000', '0.00100000'],
     ['19120.23000000', '0.07545000'], ['19120.28000000', '0.24000000'], ['19120.30000000', '0.00603000'],
     ['19120.61000000', '0.01599000'], ['19120.74000000', '0.57557000'], ['19120.91000000', '0.48747000'],
     ['19121.17000000', '1.36371000'], ['19121.46000000', '0.00059000'], ['19121.77000000', '0.05765000'],
     ['19121.87000000', '0.00579000'], ['19121.90000000', '0.26157000'], ['19122.00000000', '0.00057000'],
     ['19122.19000000', '0.01250000'], ['19122.20000000', '0.24000000'], ['19122.68000000', '0.00999000'],
     ['19122.78000000', '0.02358000'], ['19123.03000000', '2.47077000'], ['19123.52000000', '0.05261000'],
     ['19123.78000000', '0.00287000'], ['19123.81000000', '0.26157000'], ['19123.98000000', '0.00260000'],
     ['19124.06000000', '0.00060000'], ['19124.14000000', '0.27738000'], ['19124.45000000', '0.00208000'],
     ['19124.63000000', '0.00060000'], ['19124.71000000', '7.76027000'], ['19125.00000000', '0.01568000'],
     ['19125.17000000', '0.50690000'], ['19125.18000000', '0.01568000'], ['19125.43000000', '0.15000000'],
     ['19125.60000000', '0.10070000'], ['19126.00000000', '0.00074000'], ['19126.07000000', '0.26200000'],
     ['19126.08000000', '0.07606000'], ['19126.11000000', '0.00567000'], ['19126.16000000', '0.47354000'],
     ['19126.17000000', '0.47354000'], ['19126.59000000', '18.45986000'], ['19126.69000000', '0.50119000'],
     ['19126.90000000', '0.05176000'], ['19127.09000000', '0.24000000'], ['19127.11000000', '0.01312000'],
     ['19127.13000000', '0.05461000'], ['19127.18000000', '0.03144000'], ['19127.30000000', '0.47354000'],
     ['19127.69000000', '0.00523000'], ['19127.70000000', '0.40000000'], ['19127.91000000', '0.12000000'],
     ['19127.92000000', '0.12142000']]

c = time.time()


def order_book_orders(orders=a, qty=5):
    count = 0
    qty_sum = 0
    depth_sum = 0

    for depth in orders:
        # print(f'qty is {qty}')
        # print(f'float(depth[1]) is ::: {float(depth[1])}')
        if float(depth[1]) > qty:
            # print(f'qty is ::: {qty}')
            # print(f'cc is ::: {cc}')
            depth_sum += (float(depth[0]) * qty)
            # print(f"Math is {(float(depth[0]) * qty)}")
            qty_sum += qty
            # print(f'cc is {cc}')
            # print(f'dd is {dd}')
            # print(f'qty is {qty}')
            # print(f'avr is {cc / dd}')
            # print(f'-------------------------------------------------')
            # print(f'=================================================')
            break

        qty_sum -= float(depth[1])
        if qty <= 0:
            break
        # print(f'qty is ::: {qty}')
        print(count)
        # print(f'cc is ::: {cc}')
        depth_sum += (float(depth[0]) * float(depth[1]))
        # print(f"Math is {(float(depth[0]) * float(depth[1]))}")
        qty_sum += float(depth[1])
        # print(f'cc is {cc}')
        # print(f'dd is {dd}')
        # print(f'qty is {qty}')
        # print(f'avr is {cc / dd}')
        # print(f'-------------------------------------------------')
        # print(f'=================================================')

        count += 1

    print(time.time() - c)


print(order_book_orders())

'''
76428.384126+13.954117899999998+10845.0484345+419.773086+5407.9321558+1212.3126204
'''