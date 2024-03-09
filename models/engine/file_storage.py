#!/usr/bin/python3
""" filestorage class definition, first act """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ filestorage class, its used to manage file exports and inmports"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ create new objects and sets them with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ save to json file using the path defined earlier """
        serial_objects = {}
        for key, obj in FileStorage.__objects.items():
            serial_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serial_objects, f)

    def reload(self):
        """ import json file and convert its items to objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for obj in data.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
