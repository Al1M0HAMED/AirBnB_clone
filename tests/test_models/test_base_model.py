#!/usr/bin/python3
"""
test base model.
"""
import os
from datetime import datetime
from time import sleep
import unittest
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    test base model.
    """
    def test_attr(self):
        """
        test attributes.
        """
        bm = BaseModel
        self.assertEqual(str, type(bm.id))
        self.assertEqual(datetime, type(bm.created_at))
        self.assertEqual(datetime, type(bm.updated_at))


class TestBaseModel_to_dict(unittest.TestCase):
    """
    test to dict method.
    """
    pass


class TestBaseModel_save(unittest.TestCase):
    """
    test save method.
    """
    pass

if __name__ == "__main__":
    unittest.main()
