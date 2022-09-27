#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry():
    """
    class BaseGeometry
    public attribute area
    public instance method integer_validator
    """
    def area(self):
        """method defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validates property parameters, raises errors

        Raises:
        TypeError exception, <name> must be an integer
        ValueError exception, <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
