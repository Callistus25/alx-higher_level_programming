#!/usr/bin/python3
""" Class Square """


class Square:
    """ Attributes of the class """
    def __init__(self, size=0):
        """init method
        size = size of the square"""
        self.size = size

    @property
    def size(self):
        """ get the data """
        return self.__size

    @size.setter
    def size(self, value):
        """change the data"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area:
        function that defines an area of a square """
        return(self.__size * self.__size)
