#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the last digit (absolute value)
    last_digit = abs(number) % 10

    # Print the digit without a newline
    print("{:d}".format(last_digit), end="")

    # Return the value
    return last_digit
