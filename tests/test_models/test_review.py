#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.review import Review
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class Review that defines all common
attributes/methods for other classes
"""


class TestReview(unittest.TestCase):
    """
    class to validate tests to be done on the class Review
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = Review.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = Review.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_create_instance(self):
        """
        Testing if the instance was created well
        """
        my_review = Review()
        self.assertIsInstance(my_review, Review)
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertIsInstance(my_review.place_id, str)

        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertIsInstance(my_review.user_id, str)

        self.assertTrue(hasattr(my_review, "text"))
        self.assertIsInstance(my_review.text, str)
