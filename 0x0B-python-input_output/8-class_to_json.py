#!/usr/bin/python3
"""This defines a Python class-to-JSON function."""


def class_to_json(obj):
    """This return the dictionary rep of a simple data structure."""
    return obj.__dict__
