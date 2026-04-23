#!/usr/bin/python3
"""
cli.
"""
import os
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    hbnb clone cli
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        quit's the cmd
        """
        exit()

    def do_EOF(self, arg):
        """
        handels EOF
        """
        exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
