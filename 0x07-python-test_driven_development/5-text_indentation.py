#!/usr/bin/python3
"""This defines a function that prints a text"""

def text_indentation(text):
    """
    This function prints a text with indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    text = "\n".join(lines)
    if text[-1] == "\n" and text[-2] == "\n":
        text = text[:-2]
    print(text, end="")
