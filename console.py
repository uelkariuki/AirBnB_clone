#!/usr/bin/python3

"""
Program called console.py that contains the entry point of the
command interpreter
"""

import cmd
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

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything """
        pass

    def do_quit(self, line):
        """Quit command so as to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
