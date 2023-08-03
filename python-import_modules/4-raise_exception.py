#!/usr/bin/env python3

def raise_exception(x=""):
    
    try:
        raise TypeError(x)
    except TypeError as te:
        print(te)

if __name__ == "__main__":
    raise_exception("Exeption raised")       
   














