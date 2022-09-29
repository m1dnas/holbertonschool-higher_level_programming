#!/usr/bin/python3
"""task 4"""


def inherits_from(obj, a_class):
    """task 4"""
    return (type(obj) != a_class and issubclass(type(obj), a_class))
