#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Simple tests for City class"""

    def test_instantiation(self):
        cy = City()
        self.assertEqual(type(cy), City)

    def test_attributes_exist(self):
        cy = City()
        self.assertTrue(hasattr(cy, "id"))
        self.assertTrue(hasattr(cy, "created_at"))
        self.assertTrue(hasattr(cy, "updated_at"))

    def test_default_values(self):
        cy = City()
        self.assertEqual(cy.state_id, "")
        self.assertEqual(cy.name, "")

    def test_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_to_dict(self):
        cy = City()
        d = cy.to_dict()
        self.assertEqual(type(d), dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_str(self):
        cy = City()
        string = str(cy)
        self.assertIn("City", string)
        self.assertIn(cy.id, string)


if __name__ == "__main__":
    unittest.main()
