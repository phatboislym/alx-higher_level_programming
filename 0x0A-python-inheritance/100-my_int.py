#!/usr/bin/python3
"""
class MyInt is a subclass of class int
"""


class MyInt(int):
    """
    class is a rebel subclass of class int
    """

    def __eq__(self, other):
        """ method returns != for == """
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """ method returns == for != """
        return (int.__eq__(self, other))
