#!/usr/bin/python3

import unittest
import models
import uuid
from datetime import datetime
from unittest.mock import patch
from models.city import City
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
import sys
"""
Importing the unittest module to be used in validating Unittests
"""

"""
Unit testing for console.py, all features!
"""


class TestHBNBCommand(unittest.TestCase):
    """
    class to validate Unittests to be done on the console
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

    def test_more_show_command(self):
        """ Testing the console show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output12 = f.getvalue()

            the_id2 = output12.strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {the_id2}")
            output12 = f.getvalue()

            self.assertIn("BaseModel", output12)
            self.assertIn(the_id2, output12)

    def test_all_command(self):
        """ Testing the console all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output13 = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"all BaseModel")
            output13 = f.getvalue()

            self.assertIn("User", output13)

    def test_BaseModel_all_command(self):
        """ Testing the console BaseModel all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output14 = f.getvalue()

            self.assertIn("BaseModel", output14)
            self.assertIn("created_at", output14)

    def test_Review_all_command(self):
        """ Testing the Review.all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.all()")
            output15 = f.getvalue()

            self.assertIn("Review", output15)

    def test_User_all_command(self):
        """ Testing the User.all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.all()")
            output16 = f.getvalue()
            self.assertIn("User", output16)

    def test_Amenity_all_command(self):
        """ Testing the Amenity.all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.all()")
            output17 = f.getvalue()
            self.assertIn("Amenity", output17)

    def test_Place_all_command(self):
        """ Testing the Place.all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.all()")
            output18 = f.getvalue()
            self.assertIn("Place", output18)

    def test_BaseModel_count_command(self):
        """ Testing the BaseModel.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.count()")
            output19 = f.getvalue()

            self.assertGreater("BaseModel.count()", output19)
            self.assertIsInstance(output19, str)

    def test_User_count_command(self):
        """ Testing the User.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.count()")
            output20 = f.getvalue()

            self.assertGreater("User.count()", output20)
            self.assertIsInstance(output20, str)

    def test_State_count_command(self):
        """ Testing the State.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.count()")
            output21 = f.getvalue()

            self.assertGreater("State.count()", output21)
            self.assertIsInstance(output21, str)

    def test_Place_count_command(self):
        """ Testing the Place.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.count()")
            output22 = f.getvalue()

            self.assertGreater("Place.count()", output22)
            self.assertIsInstance(output22, str)

    def test_City_count_command(self):
        """ Testing the City.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.count()")
            output23 = f.getvalue()

            self.assertGreater("City.count()", output23)
            self.assertIsInstance(output23, str)

    def test_Amenity_count_command(self):
        """ Testing the Amenity.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.count()")
            output24 = f.getvalue()

            self.assertGreater("Amenity.count()", output24)
            self.assertIsInstance(output24, str)

    def test_Review_count_command(self):
        """ Testing the Review.count() command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.count()")
            output25 = f.getvalue()

            self.assertGreater("Review.count()", output25)
            self.assertIsInstance(output25, str)

    def test_BaseModel_show_command(self):
        """Testing the BaseModel.show command"""

        new_instance = BaseModel()
        new_instance.save()

        inst_id = new_instance.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(\"{inst_id}\")")
            output26 = f.getvalue().strip()

            the_output = str(storage.all()["BaseModel." + inst_id])

            self.assertEqual(output26, the_output)

    def test_User_show_command(self):
        """Testing the User.show command"""

        new_instance1 = User()
        new_instance1.save()

        inst_id1 = new_instance1.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(\"{inst_id1}\")")
            output27 = f.getvalue().strip()

            the_output1 = str(storage.all()["User." + inst_id1])

            self.assertEqual(output27, the_output1)

    def test_State_show_command(self):
        """Testing the State.show command"""
        new_instance2 = State()
        new_instance2.save()

        inst_id2 = new_instance2.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(\"{inst_id2}\")")
            output28 = f.getvalue().strip()

            the_output2 = str(storage.all()["State." + inst_id2])
            self.assertEqual(output28, the_output2)

    def test_City_show_command(self):
        """Testing the City.show command"""
        new_instance3 = City()
        new_instance3.save()
        inst_id3 = new_instance3.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(\"{inst_id3}\")")
            output29 = f.getvalue().strip()

            the_output3 = str(storage.all()["City." + inst_id3])
            self.assertEqual(output29, the_output3)

    def test_Amenity_show_command(self):
        """Testing the Amenity.show command"""
        new_instance4 = Amenity()
        new_instance4.save()
        inst_id4 = new_instance4.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(\"{inst_id4}\")")
            output30 = f.getvalue().strip()

            the_output4 = str(storage.all()["Amenity." + inst_id4])
            self.assertEqual(output30, the_output4)

    def test_Place_show_command(self):
        """Testing the Place.show command"""
        new_instance5 = Place()
        new_instance5.save()
        inst_id5 = new_instance5.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(\"{inst_id5}\")")
            output31 = f.getvalue().strip()

            the_output5 = str(storage.all()["Place." + inst_id5])
            self.assertEqual(output31, the_output5)

    def test_Review_show_command(self):
        """Testing the Review.show command"""
        new_instance6 = Review()
        new_instance6.save()
        inst_id6 = new_instance6.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(\"{inst_id6}\")")

            output32 = f.getvalue().strip()
            the_output6 = str(storage.all()["Review." + inst_id6])
            self.assertEqual(output32, the_output6)

    def test_Review_destroy_command(self):
        """Testing the Review.destroy command"""
        new_instance7 = Review()
        new_instance7.save()
        inst_id7 = new_instance7.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(\"{inst_id7}\")")

            output33 = f.getvalue().strip()
            self.assertEqual(output33, '')
            the_output7 = storage.all().get("Review." + inst_id7)
            self.assertIsNone(the_output7)

    def test_BaseModel_destroy_command(self):
        """Testing the BaseModel.destroy command"""
        new_instance8 = BaseModel()
        new_instance8.save()
        inst_id8 = new_instance8.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(\"{inst_id8}\")")

            output34 = f.getvalue().strip()
            self.assertEqual(output34, '')
            the_output8 = storage.all().get("BaseModel." + inst_id8)
            self.assertIsNone(the_output8)

    def test_User_destroy_command(self):
        """Testing the User.destroy command"""
        new_instance9 = User()
        new_instance9.save()
        inst_id9 = new_instance9.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy(\"{inst_id9}\")")

            output34 = f.getvalue().strip()
            self.assertEqual(output34, '')
            the_output8 = storage.all().get("User." + inst_id9)
            self.assertIsNone(the_output8)

    def test_City_destroy_command(self):
        """Testing the City.destroy command"""
        new_instance10 = City()
        new_instance10.save()
        inst_id10 = new_instance10.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy(\"{inst_id10}\")")

            output35 = f.getvalue().strip()
            self.assertEqual(output35, '')
            the_output8 = storage.all().get("City." + inst_id10)
            self.assertIsNone(the_output8)

    def test_State_destroy_command(self):
        """Testing the State.destroy command"""
        new_instance11 = Review()
        new_instance11.save()
        inst_id11 = new_instance11.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(\"{inst_id11}\")")

            output36 = f.getvalue().strip()
            self.assertEqual(output36, '')
            the_output9 = storage.all().get("State." + inst_id11)
            self.assertIsNone(the_output9)

    def test_Place_destroy_command(self):
        """Testing the Place.destroy command"""
        new_instance12 = Place()
        new_instance12.save()
        inst_id12 = new_instance12.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy(\"{inst_id12}\")")

            output37 = f.getvalue().strip()
            self.assertEqual(output37, '')
            the_output8 = storage.all().get("Place." + inst_id12)
            self.assertIsNone(the_output8)

    def test_Amenity_destroy_command(self):
        """Testing the Amenity.destroy command"""
        new_instance13 = Amenity()
        new_instance13.save()
        inst_id13 = new_instance13.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy(\"{inst_id13}\")")

            output38 = f.getvalue().strip()
            self.assertEqual(output38, '')
            the_output9 = storage.all().get("Amenity." + inst_id13)
            self.assertIsNone(the_output9)

    def test_BaseModel_update_command(self):
        """Testing the BaseModel.update command"""
        new_instance14 = BaseModel()
        new_instance14.save()
        inst_id14 = new_instance14.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(\"{inst_id14}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance14.name, "John")

    def test_User_update_command(self):
        """Testing the User.update command"""
        new_instance15 = User()
        new_instance15.save()
        inst_id15 = new_instance15.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(\"{inst_id15}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance15.name, "John")

    def test_State_update_command(self):
        """Testing the State.update command"""
        new_instance16 = State()
        new_instance16.save()
        inst_id16 = new_instance16.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(\"{inst_id16}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance16.name, "John")

    def test_City_update_command(self):
        """Testing the City.update command"""
        new_instance17 = City()
        new_instance17.save()
        inst_id17 = new_instance17.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(\"{inst_id17}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance17.name, "John")

    def test_Place_update_command(self):
        """Testing the Place.update command"""
        new_instance18 = Place()
        new_instance18.save()
        inst_id18 = new_instance18.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(\"{inst_id18}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance18.name, "John")

    def test_Amenity_update_command(self):
        """Testing the Amenity.update command"""
        new_instance19 = Amenity()
        new_instance19.save()
        inst_id19 = new_instance19.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update(\"{inst_id19}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance19.name, "John")

    def test_Review_update_command(self):
        """Testing the Review.update command"""
        new_instance20 = Review()
        new_instance20.save()
        inst_id20 = new_instance20.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(\"{inst_id20}\",\
 \"name\", \"John\")")

            self.assertEqual(new_instance20.name, "John")

    def test_BaseModel_update_dict_command(self):
        """Testing the BaseModel.update dict command"""
        new_instance21 = BaseModel()
        new_instance21.save()
        inst_id21 = new_instance21.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'BaseModel.update("{inst_id21}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance21.name, "John")

    def test_User_update_dict_command(self):
        """Testing the user.update dict command"""
        new_instance22 = User()
        new_instance22.save()
        inst_id22 = new_instance22.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'User.update("{inst_id22}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance22.name, "John")

    def test_State_update_dict_command(self):
        """Testing the State.update dict command"""
        new_instance23 = State()
        new_instance23.save()
        inst_id23 = new_instance23.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.update("{inst_id23}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance23.name, "John")

    def test_Amenity_update_dict_command(self):
        """Testing the Amenity.update dict command"""
        new_instance24 = Amenity()
        new_instance24.save()
        inst_id24 = new_instance24.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Amenity.update("{inst_id24}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance24.name, "John")

    def test_City_update_dict_command(self):
        """Testing the City.update dict command"""
        new_instance25 = City()
        new_instance25.save()
        inst_id25 = new_instance25.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'City.update("{inst_id25}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance25.name, "John")

    def test_Place_update_dict_command(self):
        """Testing the Place.update dict command"""
        new_instance26 = Place()
        new_instance26.save()
        inst_id26 = new_instance26.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Place.update("{inst_id26}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance26.name, "John")

    def test_Review_update_dict_command(self):
        """Testing the Review.update dict command"""
        new_instance27 = Review()
        new_instance27.save()
        inst_id27 = new_instance27.id

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'Review.update("{inst_id27}", \
                    {{"name" : "John"}})')

            self.assertEqual(new_instance27.name, "John")

    def test_City_all_command(self):
        """ Testing the City.all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.all()")
            output24 = f.getvalue()
            self.assertIn("City", output24)

    def test_State_all_command(self):
        """ Testing the State.all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'State.all()')

            output30 = f.getvalue().strip()
            self.assertEqual(output30, '')
