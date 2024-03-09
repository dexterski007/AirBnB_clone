#!/usr/bin/python3
""" testing city class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.city import City


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of city class"""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_state_in_obj(self):
        self.assertIn(City(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(City().id))

    def test_created(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(City().updated_at))


if __name__ == "__main__":
    unittest.main()
