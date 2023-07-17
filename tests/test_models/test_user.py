#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class User that inherits from BaseModel
"""


class TestUser(unittest.TestCase):
    """
    class to validate unittests to be done on the class User
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = User.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = User.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_create_User_instance(self):
        """
        Testing if the instance was created well
        """
        my_User = User()
        self.assertIsInstance(my_User, User)
        self.assertTrue(hasattr(my_User, "email"))
        self.assertIsInstance(my_User.email, str)

        self.assertTrue(hasattr(my_User, "password"))
        self.assertIsInstance(my_User.password, str)

        self.assertTrue(hasattr(my_User, "first_name"))
        self.assertIsInstance(my_User.first_name, str)

        self.assertTrue(hasattr(my_User, "last_name"))
        self.assertIsInstance(my_User.last_name, str)
