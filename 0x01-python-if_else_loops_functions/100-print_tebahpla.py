#!/usr/bin/env python3

for i in range(ord('z'), ord('A') - 1, -1):
    char = chr(i)
    if i % 2 != 0:
        char = char.upper()
    print("{}".format(char), end="")
print()
