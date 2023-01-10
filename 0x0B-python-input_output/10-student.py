#!/usr/bin/python3
""" Class Student """


class Student:
    """ Class Student init """
    def __init__(self, first_name, last_name, age):
        """ init of the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary from Student"""
        data = {}
        obj = self.__dict__
        if attrs is not None:
            for x in attrs:
                if x in obj:
                    data[x] = obj[x]
            return data
        else:
            return obj

    def reload_from_json(self, json):
        """ Reload attributes"""
        for key in json:
            setattr(self, key, json[key])
