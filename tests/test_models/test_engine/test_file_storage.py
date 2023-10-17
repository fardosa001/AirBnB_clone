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
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 7)

    def test_new(self):
        """test for new created"""
        self.storage.new(self.user)
        objects = self.storage.all()
        self.assertEqual(len(objects), 8)

    def test_save(self):
        """test for save method"""
        self.storage.new(self.user)
        self.storage.save()
        self.assertTrue(os.path.exists(self.path))

    def test_reload(self):
        """test for reload method"""
        self.storage.new(self.user)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 9)


if __name__ == '__main__':
    unittest.main()
