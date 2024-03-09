#!/usr/bin/python3
""" test for base_model.py """

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_inst(unittest.TestCase):
    """ test instantiation """

    def test_storin(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at_is_time(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_dateime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_noargs(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_unique(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_diff_created_at(self):
        basemodel1 = BaseModel()
        sleep(0.1)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, basemodel2.created_at)

    def test_diff_updated_at(self):
        basemodel1 = BaseModel()
        sleep(0.1)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, basemodel2.updated_at)

    def test_str_repr(self):
        date_time = datetime.now()
        dt_repr = repr(date_time)
        basemod = BaseModel()
        basemod.id = "213454864"
        basemod.created_at = basemod.updated_at = date_time
        bmstr = basemod.__str__()
        self.assertIn("[BaseModel] (213454864)", bmstr)
        self.assertIn("'id': '213454864'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_withoutargs(self):
        basemod = BaseModel(None)
        self.assertNotIn(None, basemod.__dict__.values())

    def test_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        basemod = BaseModel(id="546531", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(basemod.id, "546531")
        self.assertEqual(basemod.created_at, date_time)
        self.assertEqual(basemod.updated_at, date_time)

    def test_withoutkwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_kwargs(self):
        date_time = datetime.now()
        date_iso = date_time.isoformat()
        basemod = BaseModel("51", id="1321354", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(basemod.id, "1321354")
        self.assertEqual(basemod.created_at, date_time)
        self.assertEqual(basemod.updated_at, date_time)


class TestBaseModel_save(unittest.TestCase):
    """ test save method """

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

    def test_save1(self):
        basemod = BaseModel()
        sleep(0.1)
        f_updated_at = basemod.updated_at
        basemod.save()
        self.assertLess(f_updated_at, basemod.updated_at)

    def test_save2(self):
        basemod = BaseModel()
        sleep(0.1)
        f_updated_at = basemod.updated_at
        basemod.save()
        s_updated_at = basemod.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.1)
        basemod.save()
        self.assertLess(s_updated_at, basemod.updated_at)

    def test_save_arg(self):
        basemod = BaseModel()
        with self.assertRaises(TypeError):
            basemod.save(None)

    def test_save_updf(self):
        basemod = BaseModel()
        basemod.save()
        bid = "BaseModel." + basemod.id
        with open("file.json", "r") as f:
            self.assertIn(bid, f.read())


class TestBaseModel_dict(unittest.TestCase):
    """ test dict """


    def test_keys(self):
        basemod = BaseModel()
        self.assertIn("id", basemod.to_dict())
        self.assertIn("created_at", basemod.to_dict())
        self.assertIn("updated_at", basemod.to_dict())
        self.assertIn("__class__", basemod.to_dict())

    def test_isdict(self):
        basemod = BaseModel()
        self.assertTrue(dict, type(basemod.to_dict()))

    def test_add_attr(self):
        basemod = BaseModel()
        basemod.name = "python"
        basemod.my_number = 55123456
        self.assertIn("name", basemod.to_dict())
        self.assertIn("my_number", basemod.to_dict())

    def test_datetimeisstr(self):
        basemod = BaseModel()
        bm_dict = basemod.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_outputdic(self):
        date_time = datetime.now()
        basemod = BaseModel()
        basemod.id = "1132454654"
        basemod.created_at = basemod.updated_at = date_time
        timedict = {
            'id': '1132454654',
            '__class__': 'BaseModel',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }
        self.assertDictEqual(basemod.to_dict(), timedict)

    def test_dict_vs_repr(self):
        basemod = BaseModel()
        self.assertNotEqual(basemod.to_dict(), basemod.__dict__)

    def test_calldict_arg(self):
        basemod = BaseModel()
        with self.assertRaises(TypeError):
            basemod.to_dict(None)


if __name__ == "__main__":
    unittest.main()
