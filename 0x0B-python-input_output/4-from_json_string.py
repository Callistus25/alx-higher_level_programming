#!/usr/bin/python3
""" jsno string to object """
import json


def from_json_string(my_str):
    """ function that returns an obj from a json string"""
    return json.loads(my_str)
