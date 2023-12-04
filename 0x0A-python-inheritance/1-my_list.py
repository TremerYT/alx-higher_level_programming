#!/usr/bin/python3
"""This inherits from list"""


class MyList(list):
    """This is a subclass of list"""
    def __init__(self):
        """This initializes the object"""
        super().__init__()

    def print_sorted(self):
        """This prints the sorted list"""
        print(sorted(self))
