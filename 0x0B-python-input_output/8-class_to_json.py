#!/usr/bin/python3
'''
To return the dictionary description with simple data structure
'''


def class_to_json(obj):
    ''' Returning dictionary description with data list for
    JSON serialization of an object '''
    return obj.__dict__
