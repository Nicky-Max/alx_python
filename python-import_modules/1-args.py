#!/usr/bin/env python3
import sys

def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 argument.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    if num_arguments == 0:
        print(".")
    else:
        for i, arg in enumerate(argv):
            print("{} : {}".format(i+1, arg))

if __name__ == "__main__":
    print_arguments(sys.argv[1:])