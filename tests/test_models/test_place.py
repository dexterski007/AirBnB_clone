#!/usr/bin/python3
""" testing place class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.place import Place
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of place class"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_user_in_obj(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_users_ids(self):
        user1 = Place()
        user2 = Place()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = Place()
        sleep(0.1)
        user2 = Place()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = Place()
        sleep(0.1)
        user2 = Place()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_email(self):
        self.assertEqual(str, type(Place.city_id))

    def test_pass(self):
        self.assertEqual(str, type(Place.user_id))

    def test_f_name(self):
        self.assertEqual(str, type(Place.name))

    def test_l_name(self):
        self.assertEqual(str, type(Place.description))

    def test_l_name(self):
        self.assertEqual(str, type(Place.description))

    def test_n_rooms(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_n_bathrooms(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_night(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_lat(self):
        self.assertEqual(float, type(Place.latitude))

    def test_long(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amen(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        place = Place()
        place.id = "6848664"
        place.created_at = place.updated_at = date_time
        user_str = place.__str__()
        self.assertIn("[Place] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        place = Place(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place.id, "66")
        self.assertEqual(place.created_at, date_time)
        self.assertEqual(place.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for place """

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
        place = Place()
        sleep(0.1)
        f_updated_at = place.updated_at
        place.save()
        self.assertLess(f_updated_at, place.updated_at)

    def test_two_saves(self):
        place = Place()
        sleep(0.1)
        f_updated_at = place.updated_at
        place.save()
        s_updated_at = place.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        place.save()
        self.assertLess(s_updated_at, place.updated_at)

    def test_save_noargs(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_file_upd(self):
        place = Place()
        place.save()
        usid = "Place." + place.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of place """

    def test_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_dict_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_dict_attr(self):
        place = Place()
        place.middle_name = "python"
        place.my_number = 666
        self.assertEqual("python", place.middle_name)
        self.assertIn("my_number", place.to_dict())

    def test_dict_str(self):
        place = Place()
        us_dict = place.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        place = Place()
        place.id = "6848664"
        place.created_at = place.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), dico)

    def test_todict_vs_dict(self):
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_dict_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)


if __name__ == "__main__":
    unittest.main()
