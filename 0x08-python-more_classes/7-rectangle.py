#!/usr/bin/python3
"""defines class Rectangle"""


class Rectangle:
    """
    class Rectangle with private instance attributes width & height
    width and height attributes have properties setter and getter
    setter properties have type and value validation with exceptions
    public instance attributes area and perimeter
    public class attributes number_of_instances and print_symbol
    initialisation, string, reprint and delete methods
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        instance initialization method

        Args:
        width (int)
        height (int)
        """
        self.width = width
        self.height = height

        self.number_of_instances = (self.number_of_instances + 1)
        self.print_symbol = '#'

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            str_rectangle = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    str_rectangle += str(self.print_symbol)
                if i < (self.__height - 1):
                    str_rectangle += '\n'
            return (str_rectangle)

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        self.number_of_instances = (self.number_of_instances - 1)

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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)
