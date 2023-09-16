#!/usr/bin/python3
# Write a function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for r in list_keys:
        new_dir[r] *= 2

    return (new_dir)
