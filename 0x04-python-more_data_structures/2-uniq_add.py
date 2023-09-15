#!/usr/bin/python3
# Write a function that adds all unique integers in a list (only once for each integer).

def uniq_add(my_list=[]):
    sum = 0
    rec_set = set(my_list)
    for number in rec_set:
        sum += number
    return sum
