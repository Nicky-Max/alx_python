#!/usr/bin/env python3
class Square:
    def __init__(self, size):
        """
        This functions allows the user to specify the size of the square at every instance

        Arg: 
           size here is a private attribute since the  size of a square is crucial for a square, many things depend of it
        """
        self.__size = size

