#!/usr/bin/python3

"""
Program called console.py that contains the entry point of the
command interpreter
"""

import cmd
import re
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models import storage
""" importing cmd module """


class HBNBCommand(cmd.Cmd):
    """ class for the command interpreter """
    prompt = "(hbnb) "
    count = 0

    def default(self, line):
        """ overiding the default way that cmd handles args"""
        if "." in line:
            # max split=1 means split on encountering the
            # first occurence of "."
            the_class_name, method = line.split(".", 1)
            if method == "all()":
                the_class_name = the_class_name.strip()
                if the_class_name in ["BaseModel", "User", "Place",
                                      "State", "City", "Amenity", "Review"]:
                    self.do_all(the_class_name)

            elif method == "count()":
                self.do_count(the_class_name)

            elif method.startswith("show(") and method.endswith(")"):
                # slicing: starts at index 5 inclusive & end at -1 exclusive
                id_segment = method[5:-1]

                self.do_show(f"{the_class_name} {id_segment}")

            elif method.startswith("destroy(") and method.endswith(")"):
                destroy_id_segment = method[8:-1]
                self.do_destroy(f"{the_class_name} {destroy_id_segment}")
            elif method.startswith("update(") and method.endswith(")"):
                args_before_split = method[7:-1].split(", ")

                # removing the double quotation marks
                new_args = [arg.strip("\"") for arg in args_before_split]
                if len(new_args) == 3:
                    self.do_update(f"{the_class_name} {new_args[0]}\
                            {new_args[1]} {new_args[2]}")

            return

    def do_create(self, arg):
        """
        Command that Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        try:
            class_obj = eval(class_name)
            instance = class_obj()
            instance.save()
            print(instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)

        cls_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return
        # remove the "" before "4545-..." to be interpreted as 4545...
        # without the quotation marks
        id_instance = args[1].strip("\"")

        try:
            class_object = eval(cls_name)
            retrieved_instances = storage.all()

            key = "{}.{}".format(cls_name, id_instance)
            Instance = retrieved_instances.get(key)

            if not Instance:
                print("** no instance found **")
                return

            print(Instance)

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)
        cls_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_instance = args[1].strip("\"")
        try:
            class_object = eval(cls_name)
            retrieved_instances = storage.all()

            key = "{}.{}".format(cls_name, id_instance)
            value = retrieved_instances.pop(key, None)
            if not value:
                print("** no instance found **")
                return
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        if len(args) >= 1:
            cls_name = args[0]
        else:
            cls_name = "BaseModel"

        list_of_objects = []
        try:
            class_object = eval(cls_name)
            retrieved_instances = storage.all(class_object)
            # for key, value in retrieved_instances.items():
            # list_of_objects.append(str(value))
            # print(list_of_objects)
            print([str(value) for value in retrieved_instances.values()])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id by
        updating or adding attribute"""
        if not arg:
            print("** class name missing **")
            return
        args = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)
        args_length = len(args)
        class_name = args[0]
        if args_length == 1:
            print("** instance id missing **")
            return
        id = args[1]
        if args_length == 2:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if args_length == 3:
            print("** value missing **")
            return
        # attribute = args[3].strip("\"")
        attribute = " ".join(args[3:]).strip("\"")
        try:
            class_object = eval(class_name)
            retrieved_dict = storage.all()

            key = "{}.{}".format(class_name, id)
            value = retrieved_dict.get(key)

            if not value:
                print("** no instance found **")
                return
            try:
                attribute = int(attribute)
            except ValueError:
                try:
                    attribute = float(attribute)
                except ValueError:
                    # attribute = attribute.replace("\"", "")
                    pass
            setattr(value, attr_name, attribute)
            value.save()
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """ retrieve the number of instances of a class:<class name>.count()
        """
        args = arg.split()
        if len(args) < 1:
            return

        cls_name = args[0]

        try:
            class_object = eval(cls_name)
            retrieved_instances = storage.all(class_object)

            number_of_instances = len(retrieved_instances)
            print(number_of_instances)

        except NameError:
            print("** class doesn't exist **")

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """Quit command so as to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
