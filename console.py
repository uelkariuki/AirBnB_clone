#!/usr/bin/python3

"""
Program called console.py that contains the entry point of the
command interpreter
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
""" importing cmd module """


class HBNBCommand(cmd.Cmd):
    """ class for the command interpreter """
    prompt = "(hbnb) "

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

        args = arg.split()
        cls_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return
        id_instance = args[1]

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

        args = arg.split()
        cls_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_instance = args[1]
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
            retrieved_instances = storage.all()
            for key, value in retrieved_instances.items():
                list_of_objects.append(str(value))
            print(list_of_objects)
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
        attribute = args[3]
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
                    attribute = attribute.replace("\"", "")
            setattr(value, attr_name, attribute)
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
