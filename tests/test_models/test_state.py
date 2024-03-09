#!/usr/bin/python3
""" testing state class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.state import State


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of state class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_state_in_obj(self):
        self.assertIn(State(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(State().id))

    def test_created(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(State().updated_at))


if __name__ == "__main__":
    unittest.main()
