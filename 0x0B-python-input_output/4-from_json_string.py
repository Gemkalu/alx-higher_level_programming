#!/usr/bin/python3
'''
To return an object represented by JSON
'''

import json


def from_json_string(my_str):
    ''' Returning an object from JSON string '''
    return json.loads(my_str)
