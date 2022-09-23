#!/usr/bin/python3
"""Task 1 of the project 'Python - more classes'"""


class Rectangle:
    """Class of the rectangle"""
    def __init__(self, width=0, height=0):
        """private instances"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """the width of the rectangle"""
        return(self.__width)

    @width.setter
    def width(self, width):
        """set the width of the rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """the height of the rectangle"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """set the height of the rectangle"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
