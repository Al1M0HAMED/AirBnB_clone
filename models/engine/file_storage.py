#!/usr/bin/python3
"""
a simple File Storage for BaseModel instances.
"""

import json
import os


class FileStorage:

    __file_path = "file.json"

    __objects = {}

    def all(self):
        """
        returns all objects.
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        adds new obj to the list.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        saves a json file from the obj list.
        """
        if FileStorage.__objects is not None and len(
                FileStorage.__objects) >= 1:
            tmp = {}
        for k, obj in FileStorage.__objects.items():
            tmp[k] = obj.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(tmp, file)

    def reload(self):
        """
        loads a list of objects from a json file.
        """
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for key, value in data.items():
                FileStorage.__objects[key] = BaseModel(**value)
