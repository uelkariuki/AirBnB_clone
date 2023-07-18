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
from models.engine.file_storage import FileStorage
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class FileStorage from models/__init__.py file
"""


class TestInit(unittest.TestCase):
    """
    class to validate unittests to be done on the models/__init__.py
    """

    def test_create_FileStorage_instance_and_attributes(self):
        """
        Testing if the instance was created well
        """
        my_storage = FileStorage()
        self.assertIsInstance(my_storage, FileStorage)
        self.assertEqual(my_storage._FileStorage__file_path, "file.json")
        self.assertGreater(len(my_storage._FileStorage__objects), 0)

    def test_FileStorage_all_method(self):
        """
        Testing all method in FileStorage
        """
        my_storage1 = FileStorage()

        my_storage_all = my_storage1.all()

        self.assertIsInstance(my_storage_all, dict)

    def test_FileStorage_new_method(self):
        """
        Testing new method in FileStorage
        """
        my_storage2 = FileStorage()
        obj_arg = BaseModel()
        my_storage_new = my_storage2.new(obj_arg)

        self.assertIn(f"BaseModel.{obj_arg.id}",
                      my_storage2._FileStorage__objects)

    def test_FileStorage_Save_method(self):
        """
        Testing save method in FileStorage
        """
        my_storage3 = FileStorage()
        obj_arg2 = BaseModel()
        my_storage_save = my_storage3.save()

        self.assertIn(f"BaseModel.{obj_arg2.id}",
                      my_storage3._FileStorage__objects)

    def test_FileStorage_Reload_method(self):
        """
        Testing Reload method in FileStorage
        """
        my_storage4 = FileStorage()
        obj_arg3 = BaseModel()
        my_storage_Reload = my_storage4.reload()

        self.assertIn(f"BaseModel.{obj_arg3.id}",
                      my_storage4._FileStorage__objects)
