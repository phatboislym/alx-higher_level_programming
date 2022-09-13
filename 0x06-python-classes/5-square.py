#!/usr/bin/python3
"""
a module, Square
defines a square.
"""


class Square:
    """
    class Square that defines a square by:
    Private instance attribute: size
    Instantiation with size (int).
    """

    def __init__(self, size=0):
        """
        initializes the square
        Args:
            size (int): the size of the new square.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the current square area
        """
        return (self.__size**2)

    def my_print(self):
        """
        prints the square with the # character
        """
        for i in range(self.__size):
            [print("#", end='') for j in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
