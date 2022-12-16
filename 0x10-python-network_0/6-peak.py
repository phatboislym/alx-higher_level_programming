#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need to go
through all numbers to find a peak)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """function returns a peak from a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    median = int(length / 2)
    peak = list_of_integers[median]
    left_list = list_of_integers[:median]
    right_list = list_of_integers[median + 1:]
    if peak > left_list[-1] and peak > right_list[0]:
        return peak
    elif peak < left_list[-1]:
        return find_peak(left_list)
    else:
        return find_peak(right_list)
