#!/usr/bin/python3
""" testing amenity class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of amenity class"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_state_in_obj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Amenity().updated_at))


if __name__ == "__main__":
    unittest.main()
