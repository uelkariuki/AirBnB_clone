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
