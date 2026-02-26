#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)

    # Iterate through the sorted list of names
    for name in sorted(names):
        # Filter out names starting with __
        if not name.startswith("__"):
            print("{:s}".format(name))
