#!/usr/bin/python3

""" Rebel Class"""


class MyInt(int):
    """ Class with inverted == an !="""
    def __ne__(self, other):
        """Override != opeartor with =="""
        return super().__eq__(other)

    def __eq__(self, other):
        """Override == opeartor with !="""
        return super().__ne__(other)
