#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args_list = sys.argv[1:]  

    print("Number of argument(s): {}:".format(num_args), end=' ')
    print("argument" if num_args == 1 else "arguments", end='')
    print(":" if num_args > 0 else ".", end='\n')

    for i, arg in enumerate(args_list, start=1):
        print("{}: {}".format(i, arg))