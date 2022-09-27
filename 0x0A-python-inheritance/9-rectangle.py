#!/usr/bin/python3
"""
class Rectagle is a subclass of class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of class BaseGeometry that defines a rectangle"""

    def __init__(self, width, height):
        """
        method initialises an instance of class Rectangle

        Args:

        width (int): width of the Rectangle.
        height (int): height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method returns the area of the object"""
        return (self.__width * self.__height)

    def __str__(self):
        """ method returns a printable string class representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
