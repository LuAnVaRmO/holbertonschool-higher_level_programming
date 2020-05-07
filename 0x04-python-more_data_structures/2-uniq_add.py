#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for current in set(my_list):
        sum += current
    return sum
