#!/usr/bin/python3
"""Square module: task 1 of the project python-classes"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """the private instance size attribute w/ some conditions"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """the method of area"""
        return self.__size * self.__size
