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
        hlp = (" help function ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_quit(self):
        hlp = " Quit command to exit the program "
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_create(self):
        hlp = (" create new instance of basemodel ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_EOF(self):
        hlp = " EOF command ctrl + D "
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_show(self):
        hlp = (" print string repr of an instance ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_destroy(self):
        hlp = (" destroys instances based on class name and id ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_all(self):
        hlp = (" print all string repr of all instances ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_count(self):
        hlp = (" count number of instances ")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(hlp, f.getvalue().strip())

    def test_h_update(self):
        hlp = (" update the instance based on class name and id ")
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



if __name__ == "__main__":
    unittest.main()
