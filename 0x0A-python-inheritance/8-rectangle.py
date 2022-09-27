#!/isr/bin/python3
"""
class Rectangle is a subclass of BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass of the BaseGeometry class that defines a rectangle """

    def __init__(self, width, height):
        """
        method initialiaes a new instance of the class Rectangle

        Args:

        width (int): width of the Rectangle
        height (int): height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
