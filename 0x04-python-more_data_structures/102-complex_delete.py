#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            delete.append(i)
    for key in delete:
        del a_dictionary[key]
    return a_dictionary
