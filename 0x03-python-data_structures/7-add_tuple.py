#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least two elements, filling with 0 if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Perform addition element-wise
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple
