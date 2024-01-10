#!/usr/bin/python3
"""Defines a function that checks if an object is an instance or inherits from a class"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherits from, a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or if obj is an instance of a class
        that inherits from a_class; otherwise False.
    """
    return isinstance(obj, a_class)

