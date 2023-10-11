#!/usr/bin/python3
'''
Read and print the contents of a file
'''


def read_file(filename=""):
    ''' reads file and prints contents '''
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
