#!/usr/bin/python3
""" console """


import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


def argdecr(arg):
    hadina = re.search(r"\{(.*?)\}", arg)
    makouf = re.search(r"\[(.*?)\]", arg)
    if hadina is None:
        if makouf:
            part = split(arg[:makouf.span()[0]])
            export = [char.strip(",") for char in part]
            export.append(makouf.group())
            return export
        else:
            return [char.strip(",") for char in split(arg)]
    else:
        part = split(arg[:hadina.span()[0]])
        export = [char.strip(",") for char in part]
        export.append(hadina.group())
        return export


class HBNBCommand(cmd.Cmd):
    """ console class """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command ctrl + D """
        print("")
        return True

    def emptyline(self):
        """ do nothing when empty line"""
        pass

    def do_help(self, arg):
        """ help function """
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """ create new instance of basemodel """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_inst = eval(arg)()
                new_inst.save()
                print(new_inst.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ print string repr of an instance """
        args = argdecr(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """ destroys instances based on class name and id """
        args = argdecr(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """ print all string repr of all instances """
        args = argdecr(arg)
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
                print(objs)

    def default(self, arg):
        """ override default behaviour """
        cmd_list = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        check = re.search(r"\.", arg)
        if check is not None:
            args = [arg[:check.span()[0]], arg[check.span()[1]:]]
            check2 = re.search(r"\((.*?)\)", args[1])
            if check2 is not None:
                cmd = [args[1][:check2.span()[0]], check2.group()[1:-1]]
                if cmd[0] in cmd_list.keys():
                    run = "{} {}".format(args[0], cmd[1])
                    return cmd_list[cmd[0]](run)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """ count number of instances """
        args = argdecr(arg)
        c = 0
        for object_dic in storage.all().values():
            if args[0] == object_dic.__class__.__name__:
                c += 1
        print(c)

    def do_update(self, arg):
        """ update the instance based on class name and id """
        args = argdecr(arg)
        object_dic = storage.all()
        if not args:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in object_dic.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = object_dic["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valt = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valt(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = object_dic["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    valt = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valt(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
