#!/usr/bin/python3
# 4-print_square.py
"""Defining a square-printing function."""


def print_square(size):
    """This prints a square with the # character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        [print("#", end="") for b in range(size)]
        print("")
