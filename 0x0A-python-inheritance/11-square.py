#!/usr/bin/python3

"""
To write a module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square"""

    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """This returns the area"""
        return self.__size ** 2

    def __str__(self):
        """This returns the  string"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
