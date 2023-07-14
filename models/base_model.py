#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes:
"""

import uuid
from models import storage
import datetime
""" importing uuid to generate random id using uuid4"""


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """ instantiation with **args and **kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.\
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ overriding the implementation of __str__"""
        """for key, value in self.__dict__.items():
            if key == "__class__":"""
        obj_dictionary = self.__dict__.copy()
        obj_dictionary.pop("__class__", None)
        obj_dictionary["created_at"] = datetime.datetime.now()
        obj_dictionary["updated_at"] = self.created_at

        return ("[{}] ({}) {}".format(__class__.__name__,
                                      self.id, obj_dictionary))

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        # self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_result = self.__dict__
        dict_result["__class__"] = __class__.__name__

        dict_result["created_at"] = self.created_at.isoformat()
        dict_result["updated_at"] = self.updated_at.isoformat()
        return dict_result
