"""
This module imports the rectangle class
"""
from rectangle import Rectangle

"""
imported class rectangle
"""
class Square(Rectangle):
    """
    this class inherits the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This  method takes in the size and cordinate of a square
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """
        This method overides the other methods
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
