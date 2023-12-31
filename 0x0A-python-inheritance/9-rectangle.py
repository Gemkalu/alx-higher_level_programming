#!/usr/bin/python3

"""
Write a module for Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        """Initalize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """This returns the  string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
