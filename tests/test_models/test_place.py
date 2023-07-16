#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.place import Place
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class Place that defines all common
attributes/methods for other classes
"""


class TestPlace(unittest.TestCase):
    """
    class to validate tests to be done on the class Place
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = Place.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = Place.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_create_instance(self):
        """
        Testing if the instance was created well
        """
        my_place = Place()
        self.assertIsInstance(my_place, Place)
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertIsInstance(my_place.city_id, str)

        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertIsInstance(my_place.user_id, str)

        self.assertIsInstance(my_place.name, str)
        self.assertTrue(hasattr(my_place, "name"))

        self.assertTrue(hasattr(my_place, "description"))
        self.assertIsInstance(my_place.description, str)

        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertIsInstance(my_place.number_rooms, int)

        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertIsInstance(my_place.number_bathrooms, int)

        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertIsInstance(my_place.max_guest, int)

        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertIsInstance(my_place.price_by_night, int)

        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertIsInstance(my_place.latitude, float)

        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertIsInstance(my_place.longitude, float)

        self.assertTrue(hasattr(my_place, "amenity_ids"))
        self.assertTrue(all(isinstance(id, str) for id in Place.amenity_ids))
