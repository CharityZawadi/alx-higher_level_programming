#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if ord('a') <= ascii_value <= ord('z'):
            # Convert lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ascii_value - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            # Print non-alphabetic characters as they are
            print("{}".format(char), end="")
    print()  # Print a new line at the end

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
