#!/usr/bin/python3
"""
test base model.
"""
import os
from datetime import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    test base model.
    """
    def test_attr(self):
        """
        test attributes.
        """
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))
        self.assertEqual(datetime, type(bm.created_at))
        self.assertEqual(datetime, type(bm.updated_at))


class TestBaseModel_to_dict(unittest.TestCase):
    """
    test to dict method.
    """
    def test_att(self):
        bm = BaseModel()
        bm.to_dict()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())


class TestBaseModel_save(unittest.TestCase):
    """
    test save method.
    """
    def test_time(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)


if __name__ == "__main__":
    unittest.main()
