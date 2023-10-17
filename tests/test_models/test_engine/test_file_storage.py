#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
import json


class TestFileStorage(unittest.TestCase):
    """class tests"""
    def setUp(self):
        """setup class"""
        self.storage = FileStorage()
        self.user = User()
        self.path = "file.json"

    def tearDown(self):
        """teardown test at the end"""
        del self.user
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """tests for all method"""
        objects = self.storage.all()
        self.assertEqual(type(objects), dict)

    def test_new(self):
        """test for new created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "3459"
        user.name = "Ali"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_save(self):
        """test for save method"""
        self.storage.new(self.user)
        self.storage.save()
        self.assertTrue(os.path.exists(self.path))

    def test_reload(self):
        """test for reload method"""
        storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
