#!/usr/bin/python3
"""
cli.
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    hbnb clone cli
    """
    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
