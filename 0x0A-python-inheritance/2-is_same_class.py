#!/usr/bin/python3
"""
function returns true or false depending on if obj is a type of a_class
"""


def is_same_class(obj, a_class):
    """
    returns True if object is exactly an instance of the specified class;
            otherwise False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is exactly an instance of a_class
        False, otherwise
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
