#!/usr/bin/python3
"""To Write a module for MyList
"""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Print the list in ascending sort."""
        print(sorted(self))
