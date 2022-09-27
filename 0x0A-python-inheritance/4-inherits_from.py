#!/usr/bin/python3
"""
function returns True if the object is an instance of a class that
                inherited (directly or indirectly) from the specified class;
                otherwise False.
"""


def inherits_from(obj, a_class):
    """
    returns True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if type(obj) == a_class:
        return (False)
    elif isinstance(obj, a_class):
        return (True)
    else:
        return (False)
