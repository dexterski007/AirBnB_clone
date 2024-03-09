#!/usr/bin/python3
""" Base model definiton this is the base of everything """
import models
from datetime import datetime
import uuid


class BaseModel:
    """ avengers first class, this is the basemodel for the entire stuff """

    def __init__(self, *args, **kwargs):
        """ init function for the basemodel function, args unused + kwargs
        Args; unused
        kwargs: key and value
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.\
                                         strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """ update updated_at using the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dictionary of the base model values """
        dictio = self.__dict__.copy()
        dictio["created_at"] = self.created_at.isoformat()
        dictio["updated_at"] = self.updated_at.isoformat()
        dictio["__class__"] = self.__class__.__name__
        return dictio

    def __str__(self):
        """ print function, its the str representation of the basemodel """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
