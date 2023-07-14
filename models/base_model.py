#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes:
"""
#from models.engine.file_storage import storage # """ importing to help link BaseModel to FileStorage"""
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
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    storage.new(self)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ overriding the implementation of __str__"""
        return ("[{}] ({}) {}".format(__class__.__name__,
                self.id, self.__dict__))


    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()
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
