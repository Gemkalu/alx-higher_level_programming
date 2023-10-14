#!/usr/bin/python3
'''
write files
'''


def write_file(filename="", text=""):
    ''' writing text to file '''
    with open(filename, 'w') as open_file:
        open_file.write(text)
        count = open_file.tell()
    return count
