#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            # Print non-alphabetic characters as they are
            print("{}".format(char), end="")
    print()  # Print a new line at the end

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
