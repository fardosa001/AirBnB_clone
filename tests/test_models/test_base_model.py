#!/usr/bin/python3
"""unittest for base model module"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
import uuid


class TestBaseModel(unittest.TestCase):
    """tests base madel class"""

    def test_init(self):
        """tests init method"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """tests str method"""
        obj = BaseModel()
        string = str(obj)
        self.assertIn('[BaseModel]', string)
        self.assertIn("{'id': '", string)
        self.assertIn("created_at': ", string)
        self.assertIn("updated_at': ", string)

    def test_save(self):
        """test for save method"""
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        """test for dictionary method"""
        obj = BaseModel()
        class_dict = obj.to_dict()
        self.assertTrue('id' in class_dict)
        self.assertTrue('created_at' in class_dict)
        self.assertTrue('updated_at' in class_dict)


if __name__ == "__main__":
    unittest.main()
