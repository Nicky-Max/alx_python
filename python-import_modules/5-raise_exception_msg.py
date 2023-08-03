#!/usr/bin/env python3
def raise_exception_msg(message=""):
    message = "C is fun" 
    try:
        raise NameError(message)
    except NameError as ne:
        print(ne)

     
