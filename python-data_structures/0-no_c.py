#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() not in ('c',):
            result += char
    return result

if __name__ == "__main__":
    test_string = "C is fun."
    new_string = no_c(test_string)
    print(new_string)
    
   