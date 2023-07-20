#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0]
    if n == 1:
        return fibonacci_numbers

    a, b = 0, 1
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(b)
        a, b = b, a + b

    return fibonacci_numbers

