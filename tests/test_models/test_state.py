#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """tests for state class"""
    def test_state_attr(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
