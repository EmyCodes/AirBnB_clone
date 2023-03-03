#!/usr/bin/python3
import json
from models import base_model
# import models

class FileStorage():
	"""Serializes to JSON file and deserializes JSON file to instances"""
	#Private class Attributes
	__file_path = "file.json"
	__objects = {}

	# Public Istance Methods
	def all(self):
		"""Returns Dictionaary Objects"""
		return self.__objects

	def new(self, obj):
		""" """
		key = f"{obj.__class__.__name__}.{obj.id}"
		self.__objects[key] = obj
	
	def save(self):
		with open(self.__file_path, "w", encoding="utf-8") as f:
			d = {k: v.to_dict() for k, v in self.__objects.items()}
			json.dump(d, f)
	
	def reload(self):
		try:
			with open(self.__file_path, "r", encoding="utf-8") as f:
				obj_dict = json.load(f)
				for o in obj_dict.values():
					cls_name = o["__class__"]
					del o["__class__"]
					self.new(eval(f"base_model.{cls_name}")(**o))

		except FileNotFoundError:
			return
		
