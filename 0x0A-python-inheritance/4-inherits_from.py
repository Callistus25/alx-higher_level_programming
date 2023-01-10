#!/usr/bin/python3
""" Function that check if an object is an inherited instance"""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance
    Arguments:
        obj {[object]}
        a_class {[class]}
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
