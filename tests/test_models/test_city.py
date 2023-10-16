#!/usr/bin/python3
"""tests for class city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """tests for class city"""
    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
