#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end="")
        else:
            print(char, end="")
    print()

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
