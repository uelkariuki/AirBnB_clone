#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class Amenity that defines all common
attributes/methods for other classes
"""


class TestAmenity(unittest.TestCase):
    """
    class to validate tests to be done on the class Amenity
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = Amenity.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = Amenity.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_create_instance(self):
        """
        Testing if the instance was created well
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertTrue(hasattr(my_amenity, "name"))
        self.assertIsInstance(my_amenity.name, str)
