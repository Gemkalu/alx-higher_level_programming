#!/usr/bin/python3
'''
The class Student that defines a student .
'''


class Student:
    ''' The Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Initializing the  Class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Returns dictionary to JSON '''
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ben = {}
            for a, b in self.__dict__.items():
                if a in attrs:
                    ben[a] = b
            return ben
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' Changes attributes '''
        for a, b in json.items():
            self.__dict__[a] = b
