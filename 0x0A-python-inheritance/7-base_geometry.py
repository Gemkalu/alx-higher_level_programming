#!/usr/bin/python3

"""
Write a module for BaseGeometry.
"""


class BaseGeometry():
    """The BaseGeometry class"""

    def area(self):
        """This raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
