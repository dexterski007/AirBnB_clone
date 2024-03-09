#!/usr/bin/python3
""" user model """
from models.base_model import BaseModel


class User(BaseModel):
    """ Users """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
