#!/usr/bin/env python3

def raise_exception():
    
    try:
        x = "string" + 5
    except TypeError as te:
        print("Exception raised")

if __name__ == "__main__":
    raise_exception()       
   














