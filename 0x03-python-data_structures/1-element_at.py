#!/usr/bin/python3
# Task 1-element_at.py


def element_at(my_list, idx):
    """This Retrives an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
