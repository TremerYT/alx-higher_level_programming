#!/usr/bin/python3
"""This Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This Represent base geometry."""

    def area(self):
        """if Not implemented."""
        raise Exception("area() is not implemented")
