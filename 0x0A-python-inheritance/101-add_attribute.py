#!/usr/bin/python3
""" module for add_attribute"""


def add_attribute(obj, name, value):
    """ add a attribute to an object if its possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
