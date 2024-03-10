#!/usr/bin/python3
""" testing for console application """
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class Test_prompt(unittest.TestCase):
    """ test the console prompt function """

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class Test_help(unittest.TestCase):
    """ test help fnction of console """

    def test_h(self):
        hlp = ("Documented commands (type help <topic>):\n"
        "========================================\n"
        "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_quit(self):
        hlp = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_create(self):
        hlp = ("create new instance of basemodel")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_EOF(self):
        hlp = "EOF command ctrl + D"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_show(self):
        hlp = ("print string repr of an instance")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_destroy(self):
        hlp = ("destroys instances based on class name and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_all(self):
        hlp = ("print all string repr of all instances")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_count(self):
        hlp = ("count number of instances")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_update(self):
        hlp = ("update the instance based on class name and id")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(hlp, f.getvalue().strip())

class Test_exit(unittest.TestCase):
    """ test methods for exiting the console """

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_ctrld(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class Test_create(unittest.TestCase):
    """ testing do_create function"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_no_class(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(check, f.getvalue().strip())

    def test_creat_wr_class(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create NewModel"))
            self.assertEqual(check, f.getvalue().strip())

    def test_creat_inv_synt(self):
        check = "*** Unknown syntax: NewModel.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NewModel.create()"))
            self.assertEqual(check, f.getvalue().strip())
        check = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_cr_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "BaseModel.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "User.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "State.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "City.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "Amenity.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "Place.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(f.getvalue().strip()))
            testing = "Review.{}".format(f.getvalue().strip())
            self.assertIn(testing, storage.all().keys())


class Test_show(unittest.TestCase):
    """ testing show method of the console """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_no_class(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_wr_class(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show NewModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NewModel.show()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_inv_class(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(check, f.getvalue().strip())

    def test_show_missin_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_show_404(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review err"))
            self.assertEqual(check, f.getvalue().strip())

    def test_show_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["BaseModel.{}".format(test)]
            cmd = "show BaseModel {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["User.{}".format(test)]
            cmd = "show User {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["State.{}".format(test)]
            cmd = "show State {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Place.{}".format(test)]
            cmd = "show Place {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["City.{}".format(test)]
            cmd = "show City {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Amenity.{}".format(test)]
            cmd = "show Amenity {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Review.{}".format(test)]
            cmd = "show Review {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())

    def test_show_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["BaseModel.{}".format(test)]
            cmd = "BaseModel.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["User.{}".format(test)]
            cmd = "User.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["State.{}".format(test)]
            cmd = "State.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Place.{}".format(test)]
            cmd = "Place.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["City.{}".format(test)]
            cmd = "City.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Amenity.{}".format(test)]
            cmd = "Amenity.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Review.{}".format(test)]
            cmd = "Review.show({})".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(objct.__str__(), f.getvalue().strip())


class Test_destroy(unittest.TestCase):
    """ test destroy function """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destr_noclass(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(check, f.getvalue().strip())

    def test_destr_inv_cls(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy NewModel"))
            self.assertEqual(check, f.getvalue().strip())

    def test_destr_miss(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(check, f.getvalue().strip())

    def test_destr_inv_cls2(self):
        check = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place err"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review err"))
            self.assertEqual(check, f.getvalue().strip())

    def test_destr_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["BaseModel.{}".format(test)]
            cmd = "destroy BaseModel {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["User.{}".format(test)]
            cmd = "show User {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["State.{}".format(test)]
            cmd = "show State {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Place.{}".format(test)]
            cmd = "show Place {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["City.{}".format(test)]
            cmd = "show City {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Amenity.{}".format(test)]
            cmd = "show Amenity {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            objct = storage.all()["Review.{}".format(test)]
            cmd = "show Review {}".format(test)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(objct, storage.all())


class Test_all(unittest.TestCase):
    """ testing do_all function of console """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_all_inv_cls(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all NewModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NewModel.all()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_all_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertIn("User", f.getvalue().strip())
            self.assertIn("State", f.getvalue().strip())
            self.assertIn("Place", f.getvalue().strip())
            self.assertIn("City", f.getvalue().strip())
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertIn("Review", f.getvalue().strip())

    def test_all_obj2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertIn("User", f.getvalue().strip())
            self.assertIn("State", f.getvalue().strip())
            self.assertIn("Place", f.getvalue().strip())
            self.assertIn("City", f.getvalue().strip())
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertIn("Review", f.getvalue().strip())

    def test_all_singl_obj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())

class Test_update(unittest.TestCase):
    """ testing update function of console"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_update_no_cls(self):
        check = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_inv_class(self):
        check = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update NewModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NewModel.update()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_miss_id(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_missing_id_dot_notation(self):
        check = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_miss_attr(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testId = f.getvalue().strip()
            testCmd = "update BaseModel {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testId = f.getvalue().strip()
            testCmd = "update User {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testId = f.getvalue().strip()
            testCmd = "update State {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testId = f.getvalue().strip()
            testCmd = "update City {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testId = f.getvalue().strip()
            testCmd = "update Amenity {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testId = f.getvalue().strip()
            testCmd = "update Place {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        check = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testId = f.getvalue().strip()
            testCmd = "BaseModel.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testId = f.getvalue().strip()
            testCmd = "User.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testId = f.getvalue().strip()
            testCmd = "State.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testId = f.getvalue().strip()
            testCmd = "City.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testId = f.getvalue().strip()
            testCmd = "Amenity.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testId = f.getvalue().strip()
            testCmd = "Place.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(check, f.getvalue().strip())

    def test_update_str(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            testId = f.getvalue().strip()
        testCmd = "update BaseModel {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            testId = f.getvalue().strip()
        testCmd = "update User {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            testId = f.getvalue().strip()
        testCmd = "update State {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            testId = f.getvalue().strip()
        testCmd = "update City {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            testId = f.getvalue().strip()
        testCmd = "update Amenity {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            testId = f.getvalue().strip()
        testCmd = "update Review {} attr_name 'attr_value'".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])

    def test_update_val_str(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            tId = f.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            tId = f.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            tId = f.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            tId = f.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            tId = f.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            tId = f.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            tId = f.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_val_int(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} max_guest 77".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(77, test_dict["max_guest"])

    def test_update_val_int_attr(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            tId = f.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 77)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(77, test_dict["max_guest"])

    def test_update_val_float(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} latitude 8.8".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(8.8, test_dict["latitude"])

    def test_update_val_float(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            tId = f.getvalue().strip()
        testCmd = "Place.update({}, latitude, 8.8)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(8.8, test_dict["latitude"])

    def test_update_val_dict(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            testId = f.getvalue().strip()
        testCmd = "update BaseModel {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            testId = f.getvalue().strip()
        testCmd = "update User {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            testId = f.getvalue().strip()
        testCmd = "update State {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            testId = f.getvalue().strip()
        testCmd = "update City {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            testId = f.getvalue().strip()
        testCmd = "update Amenity {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            testId = f.getvalue().strip()
        testCmd = "update Review {} ".format(testId)
        testCmd += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_val_dict2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            testId = f.getvalue().strip()
        testCmd = "BaseModel.update({}".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["BaseModel.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            testId = f.getvalue().strip()
        testCmd = "User.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["User.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            testId = f.getvalue().strip()
        testCmd = "State.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["State.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            testId = f.getvalue().strip()
        testCmd = "City.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["City.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            testId = f.getvalue().strip()
        testCmd = "Amenity.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Amenity.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            testId = f.getvalue().strip()
        testCmd = "Review.update({}, ".format(testId)
        testCmd += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Review.{}".format(testId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'max_guest': 77})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(77, test_dict["max_guest"])

    def test_update_val_int_dict(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'max_guest': 77})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(77, test_dict["max_guest"])

    def test_update_val_float_dict(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_val_dict_float(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            testId = f.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class Test_count(unittest.TestCase):
    """ testing count functon of console py """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_count_inv_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("NewModel.count()"))
            self.assertEqual("0", f.getvalue().strip())

    def test_countçobj(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("2", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("2", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
