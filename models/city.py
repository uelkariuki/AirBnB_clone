#!/usr/bin/python3

"""
Task 9, Write a class City that inherits from BaseModel
"""

from models.base_model import BaseModel
""" importing the BaseModel """


class City(BaseModel):
    """
    class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
