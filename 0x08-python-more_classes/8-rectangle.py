#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter width """
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ set values for width
            Args: self, value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set value for height
            Args: self, Value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ function for rectangle's area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ function for rectangle's perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((2 * self.__width) + (2 * self.height))

    def __str__(self):
        """ print string definition of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rec += str(self.print_symbol)
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        """ print a representation of object"""
        rs = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return rs

    def __del__(self):
        """ print when instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ function that compares rectangles
            Args: rect_1 : first rectangle
                  rect_2 : Second rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
