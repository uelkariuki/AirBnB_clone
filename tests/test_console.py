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

    def test_create_command(self):
        """ Testing the console create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output_1 = f.getvalue()

        the_id_1 = output_1.strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {the_id_1}")
            output_1 = f.getvalue()

            self.assertIn("Place", output_1)
            self.assertIn(the_id_1, output_1)

    def test_help_show_command(self):
        """ Testing the console help show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output_2 = f.getvalue()

            self.assertGreater(len(output_2), 0)

    def test_help_create_command(self):
        """ Testing the console help create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output3 = f.getvalue()

            self.assertGreater(len(output3), 0)

    def test_help_destroy_command(self):
        """ Testing the console help destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")

            output4 = f.getvalue()
            self.assertGreater(len(output4), 0)

    def test_help_update_command(self):
        """ Testing the console help update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")

            output5 = f.getvalue()
            self.assertGreater(len(output5), 0)

    def test_help_all_command(self):
        """ Testing the console help all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")

            output6 = f.getvalue()
            self.assertGreater(len(output6), 0)

    def test_help_review_command(self):
        """ Testing the console help review command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help Review")

            output7 = f.getvalue()
            self.assertGreater(len(output7), 0)

    def test_help_Place_command(self):
        """ Testing the console help Place command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help Place")

            output8 = f.getvalue()
            self.assertGreater(len(output8), 0)

    def test_help_State_command(self):
        """ Testing the console help State command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help State")

            output9 = f.getvalue()
            self.assertGreater(len(output9), 0)

    def test_help_City_command(self):
        """ Testing the console help City command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help City")

            output10 = f.getvalue()
            self.assertGreater(len(output10), 0)

    def test_help_Amenity_command(self):
        """ Testing the console help Amenity command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help Amenity")

            output11 = f.getvalue()
            self.assertGreater(len(output11), 0)

    def test_help_BaseModel_command(self):
        """ Testing the console help BaseModel command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help BaseModel")

            output11 = f.getvalue()
            self.assertGreater(len(output11), 0)

    def test_help_User_command(self):
        """ Testing the console help User command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help User")

            output11 = f.getvalue()
            self.assertGreater(len(output11), 0)
