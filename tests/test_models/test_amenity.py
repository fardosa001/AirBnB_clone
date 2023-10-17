#!/usr/bin/python3
"""Amenity class test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests amenity class"""
    def test_amenity_attr(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
