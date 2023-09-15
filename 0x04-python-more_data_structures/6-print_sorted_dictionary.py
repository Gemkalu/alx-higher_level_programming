#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for j in list_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
