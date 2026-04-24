#!/usr/bin/python3
"""
cli.
"""
import shlex
import os
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    hbnb clone cli
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel
    }

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

    def do_create(self, arg):
        """creates an instance"""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        cls = self.classes[args[0]]
        obj = cls()
        obj.save()
        print(obj.id)

    def emptyline(self):
        pass

    def do_show(self, arg):
        """shows instance data
        """
        import models
        args = shlex.split(arg)
        models.storage.reload()
        objects = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        obj = args[0] + "." + args[1]
        if obj not in objects:
            print("** no instance found **")
            return
        else:
            print(objects[obj])

    def do_destroy(self, arg):
        """distroy an instance
        """
        import models
        args = shlex.split(arg)
        models.storage.reload()
        objects = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        obj = args[0] + "." + args[1]
        if obj not in objects:
            print("** no instance found **")
            return
        else:
            objects.pop(obj)
            models.storage.save()

    def do_all(self, arg):
        """prints all instances of a specifec class.
        """
        import models
        objects_list = []
        args = shlex.split(arg)
        models.storage.reload()
        objects = models.storage.all()

        if len(args) == 0:
            for obj in objects.values():
                objects_list.append(obj)

        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) > 0:
            for obj in objects.values():
                if str(obj.__class__.__name__) == args[0]:
                   objects_list.append(obj)

        print(objects_list) 

    def do_update(self, arg):
        """update an instance attribute.
        """
        import models
        args = shlex.split(arg)
        objects = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = args[0] + "." + args[1]
        if obj not in objects:
            print("** no instance found **")
            return
        else:
            setattr(objects[obj], args[2], args[3])
            objects[obj].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
