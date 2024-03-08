#!/usr/bin/python3
""" filestorage """


import json
class FileStorage:
	""" filestorage class """
	__file_path = "file.json"
	__objects = {}

	def all(self):
		""" returns dict objects """
		return FileStorage.__objects

	def new(self, obj):
		""" sets object """
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		""" save to json file """
		serial_objects = {}
		for key, obj in FileStorage.__objects.items():
			serial_objects[key] = obj.to_dict()
		with open(FileStorage.__file_path, 'w') as f:
			json.dump(serial_objects, f)

	def reload(self):
		""" desizerialize to objects """
		from models.base_model import BaseModel
		try:
			with open(FileStorage.__file_path, 'r') as f:
				data = json.load(f)
				for key, obj_data in data.items():
					class_name, obj_id = key.split('.')
					clas = eval(class_name)
					obj = clas(**obj_data)
					FileStorage.__objects[key] = obj
		except FileNotFoundError:
			pass
