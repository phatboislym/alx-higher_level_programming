#!/usr/bin/python3
"""
a module, Square
defines a square.
"""


class Square:
    """
    class Square that defines a square by:
    Private instance attribute: size
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """
        initializes the square
        Args:
            size (int): the size of the new square.
        """

        self.__size = size
