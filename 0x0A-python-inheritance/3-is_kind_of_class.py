#!/usr/bin/python3
"""
function returns true or false if obj is an instance of a_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
            is an instance of a class that inherited from,
            the specified class ; otherwise False

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
