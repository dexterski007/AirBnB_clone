#!/usr/bin/python3
""" Base model def """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ avengers first class """

    def __init__(self, *args, **kwargs):
        """ init function """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.\
                                         strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """ update current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dict with values """
        dictio = self.__dict__.copy()
        dictio['created_at'] = self.created_at.isoformat()
        dictio['updated_at'] = self.updated_at.isoformat()
        dictio['__class__'] = self.__class__.__name__
        return dictio

    def __str__(self):
        """ print function """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
