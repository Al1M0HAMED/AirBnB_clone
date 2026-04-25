#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Simple tests for Amenity class"""

    def test_instantiation(self):
        am = Amenity()
        self.assertEqual(type(am), Amenity)

    def test_attributes_exist(self):
        am = Amenity()
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))

    def test_default_values(self):
        am = Amenity()
        self.assertEqual(am.name, "")

    def test_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_to_dict(self):
        am = Amenity()
        d = am.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_str(self):
        am = Amenity()
        string = str(am)
        self.assertIn("Amenity", string)
        self.assertIn(am.id, string)


if __name__ == "__main__":
    unittest.main()
