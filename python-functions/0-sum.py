#!/usr/bin/env python3

def add(a, b):
    return a + b

add = __import__('0-sum').add
print(add(1, 2))

