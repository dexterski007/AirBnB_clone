#!/usr/bin/python3
""" testing amenity class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of amenity class"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_user_in_obj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_users_ids(self):
        user1 = Amenity()
        user2 = Amenity()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = Amenity()
        sleep(0.1)
        user2 = Amenity()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = Amenity()
        sleep(0.1)
        user2 = Amenity()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_pass(self):
        self.assertEqual(str, type(Amenity.name))

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        amenity = Amenity()
        amenity.id = "6848664"
        amenity.created_at = amenity.updated_at = date_time
        user_str = amenity.__str__()
        self.assertIn("[Amenity] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        amenity = Amenity(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "66")
        self.assertEqual(amenity.created_at, date_time)
        self.assertEqual(amenity.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for amenity """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenity = Amenity()
        sleep(0.1)
        f_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(f_updated_at, amenity.updated_at)

    def test_two_saves(self):
        amenity = Amenity()
        sleep(0.1)
        f_updated_at = amenity.updated_at
        amenity.save()
        s_updated_at = amenity.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        amenity.save()
        self.assertLess(s_updated_at, amenity.updated_at)

    def test_save_noargs(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_file_upd(self):
        amenity = Amenity()
        amenity.save()
        usid = "Amenity." + amenity.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of amenity """

    def test_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_dict_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_dict_attr(self):
        amenity = Amenity()
        amenity.middle_name = "python"
        amenity.my_number = 666
        self.assertEqual("python", amenity.middle_name)
        self.assertIn("my_number", amenity.to_dict())

    def test_dict_str(self):
        amenity = Amenity()
        us_dict = amenity.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        amenity = Amenity()
        amenity.id = "6848664"
        amenity.created_at = amenity.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'Amenity',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), dico)

    def test_todict_vs_dict(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_dict_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
