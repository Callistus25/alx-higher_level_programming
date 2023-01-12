#!/usr/bin/python3
""" functionthat compare an instance of an object"""


def is_kind_of_class(obj, a_class):
    """ function that compare the instance of an object
        Args: obj = object
              a_class = instance
        Return: true if is instance, false if not """

    if not isinstance(obj, a_class):
        return False
    return True
