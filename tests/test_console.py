#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.city import City
from models import storage
from console import HBNBCommand
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for console.py, all features!
"""


class TestHBNBCommand(unittest.TestCase):
    """
    class to validate tests to be done on the console
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = HBNBCommand.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = HBNBCommand.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_show_command(self):
        """ Testing the console show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue()

        the_id = output.strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {the_id}")
            output = f.getvalue()

        self.assertIn("User", output)
        self.assertIn(the_id, output)
