#!/usr/bin/python3

"""
program called console.py that contains the entry point of the
command interpreter
"""

import cmd
""" importing cmd module """

class HBNBCommand(cmd.Cmd):
    """ class for the command interpreter """
    prompt = "(hbnb) "

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything """
        pass

    def do_quit(self, line):
        """Quit command so as to exit the program"""
        return exit

    def do_EOF(self, line):
        """EOF command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
