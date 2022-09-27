#!/usr/bin/python3
"""
class square is a subclass of class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square is a subclass of class Rectangle
    """

    def __init__(self, size):
        """
        method initialises new instances of the class

        Args:

        size (int):size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ method returns the area of the new square """
        return (super().area())

    def __str__(self):
        """ method returns a printable string class representation """
        return ("[Square] {}/{}".format(self.__size, self.__size))
