#!/usr/bin/env python3

def raise_exception():
    
    try:
        raise TypeError("Exception raised")
    except TypeError as te:
        print(te)

if __name__ == "__main__":
    raise_exception()       
   














