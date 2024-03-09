#!/usr/bin/python3
""" initialization of the project """


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
