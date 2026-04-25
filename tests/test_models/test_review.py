#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Simple tests for Review class"""

    def test_instantiation(self):
        rv = Review()
        self.assertEqual(type(rv), Review)

    def test_attributes_exist(self):
        rv = Review()
        self.assertTrue(hasattr(rv, "id"))
        self.assertTrue(hasattr(rv, "created_at"))
        self.assertTrue(hasattr(rv, "updated_at"))

    def test_default_values(self):
        rv = Review()
        self.assertEqual(rv.place_id, "")
        self.assertEqual(rv.user_id, "")
        self.assertEqual(rv.text, "")

    def test_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_to_dict(self):
        rv = Review()
        d = rv.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_str(self):
        rv = Review()
        string = str(rv)
        self.assertIn("Review", string)
        self.assertIn(rv.id, string)


if __name__ == "__main__":
    unittest.main()
