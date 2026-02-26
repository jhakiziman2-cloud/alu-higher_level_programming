#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check for correct number of arguments (script name + 3 args = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary mapping operators to functions for clean logic
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[operator](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
