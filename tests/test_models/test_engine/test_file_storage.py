#!/usr/bin/python3
"""
test file storage.
"""
import os
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    test file storage.
    """
    def test_Fs(self):
        """
        test attributes.
        """
        self.assertEqual(type(FileStorage()), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    test  methods.
    """
    import models

    def test_new(self):
        bm = BaseModel()
        self.models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, self.models.storage.all().keys())

    def test_all(self):
        """
        test save method
        """
        import models
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_all(self):
        """
        test all method
        """
        import models
        self.assertEqual(dict, type(models.storage.all()))

    def test_reload(self):
        """
        test
        """
        bm = BaseModel()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)


if __name__ == "__main__":
    unittest.main()
