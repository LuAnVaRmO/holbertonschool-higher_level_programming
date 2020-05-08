#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    data = 0
    res = 0
    for (i, j) in my_list:
        data += i * j
        res += j
    return data / res
