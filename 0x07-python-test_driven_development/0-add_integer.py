#!/usr/bin/python3
"""
Module to add two integers
"""


def add_integer(a, b=98):
    """
    Function to add two integers

    Args:
        a (int or float): First number
        b (int or float): Second number (default is 98)

    Returns:
        int: Sum of a and b (converted to integers)

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    # Example usage
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))

