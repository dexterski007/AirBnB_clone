#!/usr/bin/python3
""" testing review class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.review import Review


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of review class"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_state_in_obj(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Review().updated_at))


if __name__ == "__main__":
    unittest.main()
