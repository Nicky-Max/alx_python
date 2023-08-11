"""
This module gives the id 
"""
class Base:
    """
    class called base
    Attribute:
          __nb_objects is a private attribute assigned a value 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method returns the id either when the user defines it or not
        Arg:
           id is the value assigned None value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id =Base.__nb_objects
