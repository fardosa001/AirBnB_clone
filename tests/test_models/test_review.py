#!/usr/bin/python3
"""tests Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test review class"""
    def test_review_attr(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
