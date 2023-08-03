#!/usr/bin/env python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
    

    safe_print_division = __import__('3-safe_print_division').safe_print_division
a = 12
b = 2

result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))