#!/usr/bin/env python3
class Square:
     
     """
        This functions allows the user to specify the size of the square at every instance

        Arg: 
           size here is a private attribute since the  size of a square is crucial for a square, many things depend of it
    """
     def __init__(self, size):
        
        self.__size = size

