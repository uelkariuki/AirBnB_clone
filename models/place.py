#!/usr/bin/python3

"""
Task 9, Write a class Place that inherits from BaseModel
"""

from models.base_model import BaseModel
""" importing the BaseModel """


class Place(BaseModel):
    """
    class Place that inherits from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]

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
