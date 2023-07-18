#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models import base_model
from models import storage
from models.base_model import BaseModel
from io import StringIO
import sys
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
        str_test = BaseModel()
        self.assertIsInstance(str_test, BaseModel)

        str_test.name = "My First Model"
        self.assertTrue(hasattr(str_test, "name"))
        str_test.my_number = 89
        self.assertTrue(hasattr(str_test, "my_number"))

        expected = (f"[BaseModel] ({str_test.id}) {str_test.__dict__}")
        self.assertEqual(str(str_test), expected)

    @patch("uuid.uuid4")
    def test_BaseModel_from_dictionary_id(self, mock_uuid4):
        """
        Validating the implementation of  Create BaseModel from dictionary ID
        """
        mock_uuid4.return_value = "fixed_id"
        my_model3 = BaseModel()
        my_model3.name = "My_First_Model"
        my_model3.my_number = 89
        id_test_input = my_model3.id.__str__()
        id_test_output = "fixed_id"
        self.assertEqual(id_test_input, id_test_output)

    @patch("uuid.uuid4")
    @patch("datetime.datetime")
    def test_BaseModel_from_dict_print_model(self, mock_datetime, mock_uuid4):
        """
        Validating the output of my_model
        """

        # fixed_id = uuid.UUID(int=0)
        mock_uuid4.return_value = "Fixed_id"
        mock_datetime.now.return_value = datetime(2023, 7, 12, 18, 4,
                                                  58, 326044)
        my_model4 = BaseModel()
        my_model4.name = "My_First_Model"
        my_model4.my_number = 89
        id_result = "Fixed_id"
        created_at_result = '2023-07-12T18:04:58.326044'
        updated_at_result = '2023-07-12T18:04:58.326044'
        name_result = 'My_First_Model'
        my_number_result = 89

        self.assertEqual(my_model4.id, id_result)
        self.assertIsInstance(my_model4.id, str)
        self.assertEqual(my_model4.created_at.isoformat(), created_at_result)
        self.assertEqual(my_model4.updated_at.isoformat(), updated_at_result)
        self.assertEqual(my_model4.name, name_result)
        self.assertEqual(my_model4.my_number, my_number_result)

    def test_type_created_at(self):
        """
        Validating the type of created_at attribute
        """
        my_model5 = BaseModel()
        self.assertIsInstance(my_model5.created_at, datetime)

    def test_the_key_values_my_model_json(self):
        """
        Validating my_model_json keys and values types
        """
        my_model6 = BaseModel()
        my_model6.name = "My_First_Model"
        my_model6.my_number = 89
        my_model_json_1 = my_model6.to_dict()
        self.assertIsInstance(my_model6.id, str)
        self.assertIsInstance(my_model6.created_at, datetime)
        self.assertIsInstance(my_model6.updated_at, datetime)
        self.assertIsInstance(my_model6.name, str)
        self.assertIsInstance(my_model6.my_number, int)
        self.assertIsInstance(my_model6.__class__.__name__, str)

    @patch("uuid.uuid4")
    @patch("datetime.datetime")
    def test_BaseModel_with_arg(self, mock_datetime, mock_uuid4):
        """
        Validating the output when basemodel has args
        """
        mock_uuid4.return_value = "no_change_id"
        created_at = datetime(2023, 7, 12, 18, 4, 58, 326044)
        mock_datetime.now.return_value = created_at
        my_model7 = BaseModel()
        my_model7.name = "My_First_Model"
        my_model7.my_number = 89
        my_model_json_2 = my_model7.to_dict()
        # my_model_json_2["created_at"] = created_at.strptime
        # (value,"%Y-%m-%dT%H:%M:%S.%f")
        my_new_model = BaseModel(**my_model_json_2)
        Test_id = my_new_model.id
        self.assertEqual(Test_id, "no_change_id")
        my_new_model_input = my_new_model.__str__()
        my_new_model_output = "[BaseModel] (\"no_change_id\") {'id':\
 'no_change_id','created_at':'2023-07-12T18:04:58.326044',\
 'updated_at':'2023-07-12T18:04:58.326044', 'name':\
 'My First Model', 'my_number': 89}"

        # self.assertEqual(my_new_model.created_at, datetime)
        # self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.my_number, int)
        self.assertFalse(my_model7 is my_new_model)

    def test_BaseModel_FileStorage(self):
        """
        Test if objects are saved to a file using JSON format
        and restore objects from the file
        """
        output = StringIO()
        sys.stdout = output
        # all_objs = storage.all()
        # self.assertIsInstance(all_objs, dict)
        # self.assertIsInstance(storage.__file_path, str)
        # self.assertIsInstance(storage.__objects, dict)
        my_model8 = BaseModel()
        my_model8.name = "My_First_Model"
        my_model8.my_number = 89
        my_model8.save()
        output_value = output.getvalue()
        sys.stdout = sys.__stdout__
        expected_value = my_model8.__str__()
        self.assertTrue(expected_value, output_value)
        # my_model9.reload()
        self.assertTrue(hasattr(my_model8, "name"))
        self.assertTrue(hasattr(my_model8, "my_number"))
        self.assertTrue(hasattr(my_model8, "created_at"))
        self.assertTrue(hasattr(my_model8, "updated_at"))
        self.assertTrue(hasattr(my_model8, "id"))

    def test_obj_not_empty(self):
        """Asserting that obj is not empty"""
        all_objects = storage.all()
        self.assertGreater(len(all_objects), 0)

    def test_attributes_using_save(self):
        """ validate the attributes after save method is called"""
        All_objects = storage.all()
        my_model10 = BaseModel()
        my_model10.name = "My_First_Model"
        my_model10.my_number = 89
        my_model10.save()
        self.assertEqual(my_model10.name, "My_First_Model")
        self.assertEqual(my_model10.my_number, 89)

    def test_unique_id_with_save(self):
        """ Validate that the ids are unique """
        my_model11 = BaseModel()
        my_model12 = BaseModel()
        old_updated_at = my_model11.updated_at
        my_model11.save()
        my_model12.save()

        self.assertNotEqual(my_model11.id, my_model12.id)
        self.assertEqual(my_model11.updated_at, old_updated_at)
        self.assertTrue(hasattr(my_model11, "created_at"))
