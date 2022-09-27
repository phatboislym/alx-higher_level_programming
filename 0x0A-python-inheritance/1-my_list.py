#!/usr/bin/python3
"""
class MyList inherits from class list
"""


class MyList(list):
    """
    sub/descendant class of class list

    Args:
        list: class list
    """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        self_list = list(self)
        self_list.sort()
        print(self_list)
