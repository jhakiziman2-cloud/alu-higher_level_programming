#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensuring each tuple has at least 2 elements by padding with zeros
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Calculating the sum using the first two elements of each padded tuple
    return (a[0] + b[0], a[1] + b[1])
