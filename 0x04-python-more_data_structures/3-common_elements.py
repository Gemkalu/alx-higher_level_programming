#!/usr/bin/python3
# Write a function that returns a set of common elements in two sets.

def common_elements(set_1, set_2):
    rec_set = {a for a in set_1 if a in set_2}
    return rec_set
