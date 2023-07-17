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

    def all(self, the_class=None):
        """ public instance methods that returns the dictionary __objects"""
        if the_class is None:
            return self.__objects
        else:
            return {key: value for key, value in
                    self.__objects.items() if isinstance(value, the_class)}

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
        json_data = {}
        for key, obj in self.__objects.items():
            json_data[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_data, file)

    def reload(self):
        """
        public instance method that  deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no
        exception should be raised)
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_data = json.load(file)

                for key, obj_dict in json_data.items():
                    class_name, obj_id = key.split(".")

                    if class_name == "BaseModel":
                        from models.base_model import BaseModel
                        obj = BaseModel(**obj_dict)
                        self.new(obj)

                    if class_name == "User":
                        from models.user import User
                        obj = User(**obj_dict)
                        self.new(obj)

                    if class_name == "Place":
                        from models.place import Place
                        obj = Place(**obj_dict)
                        self.new(obj)

                    if class_name == "City":
                        from models.city import City
                        obj = City(**obj_dict)
                        self.new(obj)

                    if class_name == "Amenity":
                        from models.amenity import Amenity
                        obj = Amenity(**obj_dict)
                        self.new(obj)

                    if class_name == "Review":
                        from models.review import Review
                        obj = Review(**obj_dict)
                        self.new(obj)

        else:
            pass
