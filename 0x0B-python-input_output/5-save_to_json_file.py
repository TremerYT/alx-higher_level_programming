#!/usr/bin/python3
"""This defines a JSON file_writting function"""
import json


def save_to_json_file(my_obj, filename):
    """This writes an obj to json rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
