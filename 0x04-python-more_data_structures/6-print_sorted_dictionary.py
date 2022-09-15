#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.items())
    for keys, values in sorted_keys:
        print(f"{keys}: {values}")
