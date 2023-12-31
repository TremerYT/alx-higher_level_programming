#!/usr/bin/python3
"""This defines a text file-reading function"""


def read_file(filename=""):
    """This prints the contents of the file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
