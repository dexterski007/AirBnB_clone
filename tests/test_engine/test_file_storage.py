#!/usr/bin/python3
""" test for file_storage file and FileStorage class """

from models.engine.file_storage import FileStorage
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os



class Test_inst_filestorage(unittest.TestCase):
    """ test for filestorage instantiation """

    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_init_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_methods(unittest.TestCase):
    """ testing FileStorage methods"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_noargs(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amen = Amenity()
        review = Review()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amen)
        models.storage.new(review)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn(basemodel, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amen.id, models.storage.all().keys())
        self.assertIn(amen, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amen = Amenity()
        review = Review()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amen)
        models.storage.new(review)
        models.storage.save()
        text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + basemodel.id, text)
            self.assertIn("User." + user.id, text)
            self.assertIn("State." + state.id, text)
            self.assertIn("Place." + place.id, text)
            self.assertIn("City." + city.id, text)
            self.assertIn("Amenity." + amen.id, text)
            self.assertIn("Review." + review.id, text)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amen = Amenity()
        review = Review()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amen)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + basemodel.id, objects)
        self.assertIn("User." + user.id, objects)
        self.assertIn("State." + state.id, objects)
        self.assertIn("Place." + place.id, objects)
        self.assertIn("City." + city.id, objects)
        self.assertIn("Amenity." + amen.id, objects)
        self.assertIn("Review." + review.id, objects)

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
