#!/usr/bin/python3

"""
Task 8, Write a class User that inherits from BaseModel
"""

from models.base_model import BaseModel
""" importing the BaseModel """


class User(BaseModel):
    """
    class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init method """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """overriding the implementation of __str__
        for key, value in self.__dict__.items():
        if key == "__class__":"""

        # super().__str__()
        obj_dictionary = self.__dict__.copy()
        obj_dictionary.pop("__class__", None)
        obj_dictionary["created_at"] = self.created_at
        obj_dictionary["updated_at"] = self.updated_at
        return ("[{}] ({}) {}".format(__class__.__name__,
                                      self.id, obj_dictionary))

    def to_dict(self):

        """returns a dictionary containing all keys/values of __dict__
        of the instance"""

        # super().to_dict()
        dict_result = self.__dict__.copy()
        dict_result["__class__"] = __class__.__name__

        dict_result["created_at"] = self.created_at.isoformat()
        dict_result["updated_at"] = self.updated_at.isoformat()

        return dict_result
