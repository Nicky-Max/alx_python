#!/usr/bin/env python3


def raise_exception_msg(message=""):
    message =""
 
    try:
        raise NameError(message)
    except NameError as ne:
        print(ne)

raise_exception_msg()    
