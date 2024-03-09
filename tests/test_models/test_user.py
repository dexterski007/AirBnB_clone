#!/usr/bin/python3
""" testing user class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.user import User
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of user class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_user_in_obj(self):
        self.assertIn(User(), models.storage.all().values())

    def test_users_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        user = User()
        user.id = "6848664"
        user.created_at = user.updated_at = date_time
        user_str = user.__str__()
        self.assertIn("[User] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        user = User(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user.id, "66")
        self.assertEqual(user.created_at, date_time)
        self.assertEqual(user.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for user """

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
        user = User()
        sleep(0.1)
        f_updated_at = user.updated_at
        user.save()
        self.assertLess(f_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.1)
        f_updated_at = user.updated_at
        user.save()
        s_updated_at = user.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        user.save()
        self.assertLess(s_updated_at, user.updated_at)

    def test_save_noargs(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_file_upd(self):
        user = User()
        user.save()
        usid = "User." + user.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of user """

    def test_dict(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_dict_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_dict_attr(self):
        user = User()
        user.middle_name = "python"
        user.my_number = 666
        self.assertEqual("python", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_dict_str(self):
        user = User()
        us_dict = user.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        user = User()
        user.id = "6848664"
        user.created_at = user.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), dico)

    def test_todict_vs_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_dict_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
