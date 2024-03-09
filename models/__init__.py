#!/usr/bin/python3
""" initialization of the project, this is the way """


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
