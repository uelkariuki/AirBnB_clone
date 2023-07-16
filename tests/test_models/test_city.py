#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.city import City
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class City that defines all common
attributes/methods for other classes
"""


class TestCity(unittest.TestCase):
    """
    class to validate tests to be done on the class City
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = City.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = City.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_create_instance(self):
        """
        Testing if the instance was created well
        """
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertTrue(hasattr(my_city, "name"))
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertIsInstance(my_city.name, str)
        self.assertIsInstance(my_city.state_id, str)
