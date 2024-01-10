#!/usr/bin/python3
"""Module to load, add, and save"""

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, "add_item.json")

