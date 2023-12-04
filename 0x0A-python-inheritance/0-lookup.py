#!/usr/bin/python3
"""This function returns the list of available attributes."""


def lookup(obj):
    """This return a list of an object's available attributes."""
    return (dir(obj))
