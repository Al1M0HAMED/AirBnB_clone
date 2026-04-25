#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Simple tests for State class"""

    def test_instantiation(self):
        st = State()
        self.assertEqual(type(st), State)

    def test_attributes_exist(self):
        st = State()
        self.assertTrue(hasattr(st, "id"))
        self.assertTrue(hasattr(st, "created_at"))
        self.assertTrue(hasattr(st, "updated_at"))

    def test_name_default(self):
        st = State()
        self.assertEqual(st.name, "")

    def test_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_to_dict(self):
        st = State()
        d = st.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_str(self):
        st = State()
        string = str(st)
        self.assertIn("State", string)
        self.assertIn(st.id, string)


if __name__ == "__main__":
    unittest.main()
