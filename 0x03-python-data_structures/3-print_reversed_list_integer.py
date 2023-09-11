#!/usr/bin/python3
# Task 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """This Prints all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
