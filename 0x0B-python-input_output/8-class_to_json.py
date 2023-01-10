#!/usr/bin/python3
""" dictionary description """


def class_to_json(obj):
    """ function that returns the attributes from an obj """
    return obj.__dict__
