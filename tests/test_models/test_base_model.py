#!/usr/bin/python3

import unittest
import models
from datetime import datetime
from unittest.mock import patch
from models import base_model
from models.base_model import BaseModel
"""
Importing the unittest module to be used in validating tests
"""

"""
Unit testing for class BaseModel that defines all common
attributes/methods for other classes
"""


class TestBaseModel(unittest.TestCase):
    """
    class to validate tests to be done on the class BaseModel
    """

    def test_documentation_module(self):
        """method to check the module documentation"""
        module_doc = base_model.__doc__
        self.assertTrue(len(module_doc) > 1, "No Module documentation")

    def test_documentation_class(self):
        """method to check the class(BaseModel) documentation"""
        class_doc = BaseModel.__doc__
        self.assertTrue(len(class_doc) > 1, "No class documentation")

    def test_documentation_save_method(self):
        """method to check the method (save)documentation"""
        my_object = BaseModel()
        save_doc = my_object.save.__doc__
        self.assertTrue(len(save_doc) > 1, "No save method documentation")

    def test_documentation_to_dict_method(self):
        """method to check the method (to_dict) documentation"""
        my_object1 = BaseModel()
        to_dict_doc = my_object1.to_dict.__doc__
        self.assertTrue(len(to_dict_doc) > 1,
                        "No to_dict method documentation")

    def test_create_instance(self):
        """
        Testing if the instance was created well
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        # self.assertEqual(my_model.__str__(), '[BaseModel] (...)
        # {'updated_at': datetime.datetime(...), 'id': '...',
        # created_at': datetime.datetime(...)}')

    def test_attributes(self):
        """
        validate the presence of attributes
        """
        attr_test1 = BaseModel()
        self.assertTrue(hasattr(attr_test1, "id"))
        self.assertTrue(hasattr(attr_test1, "__class__"))

    def test_name_and_my_number_attributes(self):
        """
        Validating the addition of my_number & name attributes
        """
        my_model1 = BaseModel()
        self.assertIsInstance(my_model1, BaseModel)
        my_model1.name = "My First Model"
        self.assertTrue(hasattr(my_model1, "name"))
        my_model1.my_number = 89
        self.assertTrue(hasattr(my_model1, "my_number"))

        # self.assertEqual(my_model1.__str__(), '[BaseModel] (...)
        # {''my_number': 89, 'name': 'My First Model', updated_at':
        # datetime.datetime(...), 'id': '...',
        # 'created_at': datetime.datetime(...)}')

    def test_type_of_attributes_instances(self):
        """
        Validate the attributes instances ie my_number attribute
        is of instance int
        """
        my_Model = BaseModel()
        my_Model.name = "My First Model"
        my_Model.my_number = 89
        self.assertIsInstance(my_Model.name, str)
        self.assertIsInstance(my_Model.my_number, int)
        self.assertIsInstance(my_Model.id, str)
        self.assertIsInstance(my_Model.updated_at, datetime)
        self.assertIsInstance(my_Model.created_at, datetime)

    def test_save_method(self):
        """
        Validating the implementation of the save method
        """
        my_Model_Save = BaseModel()
        my_Model_Save.save()
        self.assertTrue(hasattr(my_Model_Save, "id"))
        self.assertTrue(hasattr(my_Model_Save, "updated_at"))
        self.assertTrue(hasattr(my_Model_Save, "created_at"))

        # self.assertEqual(my_model1.__str__(), '[BaseModel] (...)
        # {''my_number': 89, 'name': 'My First Model', updated_at':
        # datetime.datetime(...), 'id': '...', 'created_at':
        # datetime.datetime(...)}')

    @patch("uuid.uuid4")
    @patch("datetime.datetime")
    def test_to_dict_method(self, mock_datetime, mock_uuid4):
        """
        Validating the implementation of to_dict method
        """

        mock_uuid4.return_value = "no_change_id"
        mock_datetime.now.return_value = datetime(2023, 7, 12, 18, 4,
                                                  58, 326044)
        dict1 = BaseModel()
        dict1.name = "My First Model"
        dict1.my_number = 89
        my_model_json = dict1.to_dict()

        wanted_result = {'id': 'no_change_id', 'created_at':
                         '2023-07-12T18:04:58.326044', 'updated_at':
                         '2023-07-12T18:04:58.326044', 'name':
                         'My First Model', 'my_number': 89,
                         '__class__': 'BaseModel'}
        self.assertEqual(my_model_json, wanted_result)
    # def test_my_model_json_key_and_values(self):
        # """
        # Validating the keys and values(its type inclusive) of my_model_json
        # """
        # for key in my_model_json.keys():

        # self.assertEqual(my_model_json.__str__(),
        # '\t my_number: (<class 'int'>) - 89
        # \t name: (<class 'str'>) - My First Model
        # \t __class__: (<class 'str'>) - BaseModel
        # \t updated_at: (<class 'str'>) - ...
        # \t id: (<class 'str'>) - ...
        # \t created_at: (<class 'str'>) - ...')

    def test_uuid(self):
        """
        Validate that uuid is implemented properly
        """
        BModel1 = BaseModel()
        BModel2 = BaseModel()

        self.assertIsInstance(BModel1, BaseModel)
        self.assertIsInstance(BModel2, BaseModel)

        self.assertTrue(hasattr(BModel1, "id"))
        self.assertTrue(hasattr(BModel2, "id"))

        self.assertNotEqual(BModel1.id, BModel2.id)

        self.assertIsInstance(BModel1.id, str)
        self.assertIsInstance(BModel2.id, str)

    @patch("uuid.uuid4")
    def test_uuid_values(self, mock_uuid4):
        """
        testing the id values to see if uuid.uuid(4) is working well
        """
        mock_uuid4.return_value = "no_change_id"

        tester_uuid = BaseModel()
        self.assertEqual(tester_uuid.id, "no_change_id")

    def test_string_representation(self):
        """
        Validating the overwritten string representation __str__
        works
        """
        str_testing = BaseModel()
        self.assertIsInstance(str_testing, BaseModel)

        str_testing.name = "My First Model"
        self.assertTrue(hasattr(str_testing, "name"))
        str_testing.my_number = 89
        self.assertTrue(hasattr(str_testing, "my_number"))

        # self.assertEqual(str_testing.__str__(),\
        # '[BaseModel] (...) {''my_number': 89,\
        # name': 'My First Model', updated_at':
        # datetime.datetime(...), 'id': '...', 'created_at':
        # datetime.datetime(...)}')
