#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in my_list:
        if i % 2:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list