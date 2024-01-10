#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))

