#!/usr/bin/python3
""" testing city class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.city import City
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of city class"""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_user_in_obj(self):
        self.assertIn(City(), models.storage.all().values())

    def test_users_ids(self):
        user1 = City()
        user2 = City()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = City()
        sleep(0.1)
        user2 = City()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = City()
        sleep(0.1)
        user2 = City()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        self.assertEqual(str, type(City().id))

    def test_created(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_email(self):
        self.assertEqual(str, type(City.state_id))

    def test_pass(self):
        self.assertEqual(str, type(City.name))

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        city = City()
        city.id = "6848664"
        city.created_at = city.updated_at = date_time
        user_str = city.__str__()
        self.assertIn("[City] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        city = City(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city.id, "66")
        self.assertEqual(city.created_at, date_time)
        self.assertEqual(city.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for city """

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
        city = City()
        sleep(0.1)
        f_updated_at = city.updated_at
        city.save()
        self.assertLess(f_updated_at, city.updated_at)

    def test_two_saves(self):
        city = City()
        sleep(0.1)
        f_updated_at = city.updated_at
        city.save()
        s_updated_at = city.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        city.save()
        self.assertLess(s_updated_at, city.updated_at)

    def test_save_noargs(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_file_upd(self):
        city = City()
        city.save()
        usid = "City." + city.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of city """

    def test_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_dict_attr(self):
        city = City()
        city.middle_name = "python"
        city.my_number = 666
        self.assertEqual("python", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_dict_str(self):
        city = City()
        us_dict = city.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        city = City()
        city.id = "6848664"
        city.created_at = city.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'City',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), dico)

    def test_todict_vs_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_dict_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
