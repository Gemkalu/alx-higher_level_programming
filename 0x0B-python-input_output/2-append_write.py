#!/usr/bin/python3
'''
This appends text to file
'''


def append_write(filename="", text=""):
    ''' appends text to file '''
    with open(filename, 'a') as open_file:
        count = open_file.write(text)
    return count
