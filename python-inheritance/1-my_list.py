#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """create a new list in ascending sort"""
        print(sorted(self))
