#!/usr/bin/env python3
class Square:
    """
    This class defines a square by a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
print(__import__("0-square").Square.__doc__)
print(__import__("0-square").Square.__init__.__doc__)      

