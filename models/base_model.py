#!/usr/bin/python3
"""
Base model.
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    base model class.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):

        return (
            "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__))

    def save(self):
        """
        saves new date.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns dict representaion.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
