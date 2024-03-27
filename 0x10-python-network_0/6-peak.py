#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    mid = n // 2
    peak = list_of_integers[mid]

    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
            (mid == n - 1 or peak >= list_of_integers[mid + 1]):
        return peak

    if mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])


# Test cases
if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 4 or 3
    print(find_peak([2, 2, 2]))  # Output: 2
    print(find_peak([]))  # Output: None
    print(find_peak([-2, -4, 2, 1]))  # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4
