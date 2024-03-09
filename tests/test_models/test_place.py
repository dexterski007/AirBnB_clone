#!/usr/bin/python3
""" testing place class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.place import Place


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of place class"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_state_in_obj(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Place().updated_at))


if __name__ == "__main__":
    unittest.main()
