#!/usr/local/bin/python3
""" find peak of a list """


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    if list_of_integers:
        peak = list_of_integers[0]
        for i in range(1, size):
            if list_of_integers[i - 1] < list_of_integers[i] > list_of_integers[i + 1]:
                peak = (list_of_integers[i])
                if peak < list_of_integers[0]:
                    peak = list_of_integers[0]
        return peak
