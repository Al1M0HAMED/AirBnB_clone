#!/usr/bin/python3
"""
a simple File Storage for BaseModel instances.
"""
from models.base_model import BaseModel
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
        tmp = {}
        for k, obj in FileStorage.__objects.items():
            tmp[k] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(tmp, file)

    def reload(self):
        """
        loads a list of objects from a json file.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            classes = {
                "BaseModel": BaseModel
            }
            for key, value in data.items():
                cls_name = value.get("__class__")
                if not cls_name:
                    continue
                cls = classes.get(cls_name)
                if cls:
                    FileStorage.new(cls(**value))
