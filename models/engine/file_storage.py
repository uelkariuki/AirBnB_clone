#!/usr/bin/python3

import json
import os
""" importing the json module"""

"""
class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances
"""

class FileStorage:
    """ class FileStorage"""
    """ private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ public instance methods that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ public instance methods that sets in __objects the
        obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ 
        public instance method that serializes __objects to
        the JSON file (path: __file_path)
        """
        
        json_data = json.dumps(self.__objects, default=lambda obj: obj.to_dict())
        json_file_path = self.__file_path
        with open(json_file_path, "w") as file:
            file.write(json_data)

    def reload(self):
        """
        public instance method that  deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no
        exception should be raised)
        """
        #self.__objects = {}
        file_path = self.__file_path

        if file_path is not None and os.path.exists(file_path):
            with open(file_path, "r") as file: #try:
                read_data = file.read()
                if read_data:
                    self.__objects = json.loads(read_data)
                #except json.JSONDecodeError:
                    #self.__objects = {}
        else:
            pass
