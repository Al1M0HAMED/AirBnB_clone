#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Simple tests for Place class"""

    def test_instantiation(self):
        pl = Place()
        self.assertEqual(type(pl), Place)

    def test_attributes_exist(self):
        pl = Place()
        self.assertTrue(hasattr(pl, "id"))
        self.assertTrue(hasattr(pl, "created_at"))
        self.assertTrue(hasattr(pl, "updated_at"))

    def test_default_values(self):
        pl = Place()
        self.assertEqual(pl.city_id, "")
        self.assertEqual(pl.user_id, "")
        self.assertEqual(pl.name, "")
        self.assertEqual(pl.description, "")

        self.assertEqual(pl.number_rooms, 0)
        self.assertEqual(pl.number_bathrooms, 0)
        self.assertEqual(pl.max_guest, 0)
        self.assertEqual(pl.price_by_night, 0)

        self.assertEqual(pl.latitude, 0.0)
        self.assertEqual(pl.longitude, 0.0)

        self.assertEqual(pl.amenity_ids, [])

    def test_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_to_dict(self):
        pl = Place()
        d = pl.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_str(self):
        pl = Place()
        string = str(pl)
        self.assertIn("Place", string)
        self.assertIn(pl.id, string)


if __name__ == "__main__":
    unittest.main()
