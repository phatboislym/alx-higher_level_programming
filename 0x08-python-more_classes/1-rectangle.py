#!/usr/bin/python3
"""defines class Rectangle"""


class Rectangle:
    """
    class Rectangle with private instance attributes width & height
    attributes have properties setter and getter
    setter properties have type and value validation with exceptions
    """
    def __init__(self, width=0, height=0):
        """
        instance initialization method

        Args:
        width (int)
        height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value: int):
        if not (isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value: int):
        if not (isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
