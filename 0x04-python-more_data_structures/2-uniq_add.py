#!/usr/bin/python3
# Write a function that adds all unique integers in a list (only once for each integer).

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
