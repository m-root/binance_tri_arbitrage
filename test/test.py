arr = [[6, 1], [1, 2], [3, 4], [5, 6], [2, 3], [4, 5]]
'''
start_item = 1 or a and pair is b
array with start item = last_item 
pair_part of start_item = b
'''

def separator(ab, b):
    if b.index(ab) == 0:
        return b[1]
    else:
        return b[0]
import time

def pair_sorting(start_item = 1, array_edit = arr):
    new_arr = []
    time_start = time.time()
    print(time_start)
    while len(array_edit) > 0:
        for aa in array_edit:
            if start_item not in aa:
                aa = [b for b in array_edit if start_item in b][0]
                print(aa)
            ans = separator(start_item, aa)
            print(ans)
            array_edit.remove(aa)
            start_item = ans
            new_arr.append(aa)
    print(time.time()-time_start)
    print(new_arr)
    return new_arr

pair_sorting()