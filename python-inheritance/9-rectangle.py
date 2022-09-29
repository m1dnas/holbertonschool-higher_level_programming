#!/usr/bin/python3
"""task 9"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ with super, I'm calling the method from Rectangle's superclass """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """ definfing area """
    def area(self):
        super().__init__()
        """ calculating the area of a rectangle """
        return self.__width * self.__height

    """ defining string representation """
    def __str__(self):
        """ styling the string representation of the object """
        return f'[Rectangle] {self.__width}/{self.__height}'
        # f-Strings format
