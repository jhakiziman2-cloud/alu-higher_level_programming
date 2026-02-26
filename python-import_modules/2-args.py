#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the list of arguments excluding the script name
    args = sys.argv[1:]
    count = len(args)

    # Determine the correct pluralization and punctuation
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    # Print each argument with its position
    for i in range(count):
        print("{:d}: {:s}".format(i + 1, args[i]))
