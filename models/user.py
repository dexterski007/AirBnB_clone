#!/usr/bin/python3
""" user model based on basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ represeentation of user based on BaseModel with mail pass nd names """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
