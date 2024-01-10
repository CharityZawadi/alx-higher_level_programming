#!/usr/bin/python3
"""
Module to print a square with the character #
"""


def print_square(size):
    """
    Function to print a square with the character #

    Args:
        size (int): Size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    # Example usage
    print_square(4)

