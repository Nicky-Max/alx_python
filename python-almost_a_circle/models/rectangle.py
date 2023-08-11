"""
This module imports Base class from the base module

"""

from models.base import Base
"""
from the module base we imported Base class
"""

class Rectangle(Base):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle's position.
            y: The y-coordinate of the rectangle's position.
            id: The ID of the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        This getter method is used to retrive values of the attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This setter method modifies the value of the width
        """
        self.__width = value

    @property
    def height(self):
        """
        This getter method is used to retrive values of the attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This setter method modifies the value of the height
        """
        self.__height = value

    @property
    def x(self):
        """
        This getter method is used to retrive values of the attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This setter method modifies the value of the x
        """
        self.__x = value

    @property
    def y(self):
        """
        This getter method is used to retrive values of the attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This setter method modifies the value of the y
        """
        self.__y = value