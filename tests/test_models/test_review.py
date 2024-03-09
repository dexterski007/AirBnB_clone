#!/usr/bin/python3
""" testing review class which inherits basemodel class """
import models
import unittest
from datetime import datetime
from models.review import Review
from time import sleep
import os


class TestUser_inst(unittest.TestCase):
    """ testing instantiation of review class"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_user_in_obj(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_users_ids(self):
        user1 = Review()
        user2 = Review()
        self.assertNotEqual(user1.id, user2.id)

    def test_users_created(self):
        user1 = Review()
        sleep(0.1)
        user2 = Review()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated(self):
        user1 = Review()
        sleep(0.1)
        user2 = Review()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_email(self):
        self.assertEqual(str, type(Review.place_id))

    def test_pass(self):
        self.assertEqual(str, type(Review.user_id))

    def test_f_name(self):
        self.assertEqual(str, type(Review.text))

    def test_str(self):
        date_time = datetime.now()
        date_rep = repr(date_time)
        review = Review()
        review.id = "6848664"
        review.created_at = review.updated_at = date_time
        user_str = review.__str__()
        self.assertIn("[Review] (6848664)", user_str)
        self.assertIn("'id': '6848664'", user_str)
        self.assertIn("'created_at': " + date_rep, user_str)
        self.assertIn("'updated_at': " + date_rep, user_str)

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        review = Review(id="66", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(review.id, "66")
        self.assertEqual(review.created_at, date_time)
        self.assertEqual(review.updated_at, date_time)

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class Test_save_user(unittest.TestCase):
    """ test save function for review """

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
        review = Review()
        sleep(0.1)
        f_updated_at = review.updated_at
        review.save()
        self.assertLess(f_updated_at, review.updated_at)

    def test_two_saves(self):
        review = Review()
        sleep(0.1)
        f_updated_at = review.updated_at
        review.save()
        s_updated_at = review.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        review.save()
        self.assertLess(s_updated_at, review.updated_at)

    def test_save_noargs(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_file_upd(self):
        review = Review()
        review.save()
        usid = "Review." + review.id
        with open("file.json", "r") as file:
            self.assertIn(usid, file.read())


class Test_user_dict(unittest.TestCase):
    """ test export to dict function of review """

    def test_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_dict_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_dict_attr(self):
        review = Review()
        review.middle_name = "python"
        review.my_number = 666
        self.assertEqual("python", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_dict_str(self):
        review = Review()
        us_dict = review.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_dict_out(self):
        date_time = datetime.now()
        review = Review()
        review.id = "6848664"
        review.created_at = review.updated_at = date_time
        dico = {
            'id': '6848664',
            '__class__': 'Review',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), dico)

    def test_todict_vs_dict(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_dict_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
