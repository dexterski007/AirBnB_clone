#!/usr/bin/python3
""" testing state class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.state import State
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of state class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_user_in_obj(self):
        self.assertIn(State(), models.storage.all().values())

    def test_users_ids(self):
        user1 = State()
        user2 = State()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = State()
        sleep(0.1)
        user2 = State()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = State()
        sleep(0.1)
        user2 = State()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        self.assertEqual(str, type(State().id))

    def test_created(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_f_name(self):
        self.assertEqual(str, type(State.name))

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        state = State()
        state.id = "6848664"
        state.created_at = state.updated_at = date_time
        user_str = state.__str__()
        self.assertIn("[State] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        state = State(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "66")
        self.assertEqual(state.created_at, date_time)
        self.assertEqual(state.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for state """

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
        state = State()
        sleep(0.1)
        f_updated_at = state.updated_at
        state.save()
        self.assertLess(f_updated_at, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.1)
        f_updated_at = state.updated_at
        state.save()
        s_updated_at = state.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        state.save()
        self.assertLess(s_updated_at, state.updated_at)

    def test_save_noargs(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_file_upd(self):
        state = State()
        state.save()
        usid = "State." + state.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of state """

    def test_dict(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_dict_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_dict_attr(self):
        state = State()
        state.middle_name = "python"
        state.my_number = 666
        self.assertEqual("python", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_dict_str(self):
        state = State()
        us_dict = state.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        state = State()
        state.id = "6848664"
        state.created_at = state.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'State',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), dico)

    def test_todict_vs_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_dict_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
