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
        return (self.__objects)

    def new(self, obj):
        """
        adds new obj to the list.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        saves a json file from the obj list.
        """
        if self.__objects is not None and len(self.__objects) >= 1:
            tmp = {}
        for k, obj in self.__objects.items():
            tmp[k] = obj.to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(tmp, file)

    def reload(self):
        """
        loads a list of objects from a json file.
        """
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for key, value in data.items():
                self.__objects[key] = BaseModel(**value)
