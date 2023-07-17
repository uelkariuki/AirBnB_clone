#!/usr/bin/python3

"""
Task 9, Write a class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel
""" importing the BaseModel """


class Amenity(BaseModel):
    """
    class Amenity that inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method """
        super().__init__(*args, **kwargs)
