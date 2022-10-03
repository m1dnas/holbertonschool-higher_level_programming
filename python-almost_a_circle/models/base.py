#!/usr/bin/python3
"""
Module that define the base class of the project 'Almost a circle'
"""


class Base:
    """this class'll be the 'base' of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
