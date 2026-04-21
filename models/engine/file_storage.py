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
        return (self.__objects)

    def new(self, obj):
        obj_dict = obj.to_dict()
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj_dict

    def save(self):
        if self.__objects is not None and len(self.__objects) >= 1:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(self.__objects, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
