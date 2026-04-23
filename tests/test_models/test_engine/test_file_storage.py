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
    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
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

    def test_save(self):
        """
        test save method
        """
        import models
        with self.assertRaises(TypeError):
            models.storage.save(None)
        bm = BaseModel()
        self.models.storage.new(bm)
        self.models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_all(self):
        """
        test all method
        """
        import models
        self.assertEqual(dict, type(models.storage.all()))

    def test_reload(self):
        """
        test reload method
        """
        import models
        bm = BaseModel()
        objs = FileStorage._FileStorage__objects
        models.storage.save()
        models.storage.reload()
        models.storage._FileStorage__objects = {}
        self.assertIn("BaseModel." + bm.id, objs)


if __name__ == "__main__":
    unittest.main()
