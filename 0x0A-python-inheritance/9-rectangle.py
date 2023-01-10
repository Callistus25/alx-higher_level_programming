#!/usr/bin/python3
"""Class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Child from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ fuction that defines the area"""
        return self.__width * self.__height

    def __str__(self):
        """ Function str to print"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
