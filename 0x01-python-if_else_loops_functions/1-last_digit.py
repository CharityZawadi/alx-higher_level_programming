#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
prefix = "Last digit of"
comparison = "and is"

if number < 0:
    last_digit *= -1  # Make the last digit negative if the original number is negative

if last_digit > 5:
    print(f"{prefix} {number} is {last_digit} {comparison} greater than 5")
elif last_digit == 0:
    print(f"{prefix} {number} is {last_digit} {comparison} 0")
else:
    print(f"{prefix} {number} is {last_digit} {comparison}less than 6 and not 0")
