#!/usr/bin/python3

"""
Task 9, Write a class Review that inherits from BaseModel
"""

from models.base_model import BaseModel
""" importing the BaseModel """


class Review(BaseModel):
    """
    class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
