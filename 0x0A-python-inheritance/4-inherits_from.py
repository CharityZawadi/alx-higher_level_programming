#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class"""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj inherits from a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

