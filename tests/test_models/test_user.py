"""Tests for class user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class"""
    def test_user_attr(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
