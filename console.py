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
        args = arg.split()
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
        args = arg.split()
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
        args = arg.split()
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
        args = arg.split()
        c = 0
        for obj in storage.all().values():
            if args[0] == obj.__class.__name__:
                c += 1
        print(c)

    def do_update(self, arg):
        """ update the instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            object_dic = storage.all().get(key)
            if object_dic is None:
                print("** no instance found **")
            else:
                setattr(object_dic, args[2], args[3])
                object_dic.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
