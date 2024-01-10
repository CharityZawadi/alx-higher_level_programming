#!/usr/bin/python3
"""
Module to print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print "My name is <first name> <last name>"

    Args:
        first_name (str): First name
        last_name (str): Last name (default is "")

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted message
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    # Example usage
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

