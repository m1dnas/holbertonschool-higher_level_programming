#!/usr/bin/python3
"""task 3"""


def is_kind_of_class(obj, a_class):
    """isinstance to check an instance's type of obj"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
