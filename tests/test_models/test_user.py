#!/usr/bin/python3
"""test user
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user"""
    def test_create_user(self):
        """test user"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_has_id(self):
        """test user"""
        user = User()
        self.assertIsInstance(user.id, str)

    def test_user_has_dates(self):
        """test user"""
        user = User()
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_attributes(self):
        """test user"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_save_updates_time(self):
        """test user"""
        user = User()
        old_time = user.updated_at
        user.save()
        self.assertNotEqual(old_time, user.updated_at)

    def test_to_dict(self):
        """test user"""
        user = User()
        d = user.to_dict()

        self.assertIsInstance(d, dict)
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)


if __name__ == "__main__":
    unittest.main()
