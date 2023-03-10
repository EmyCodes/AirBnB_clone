#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
	"""Public Instance here"""
	def __init__(self, *args, **kwargs):
		"""Initializing"""
		if len(kwargs) != 0:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key == "created_at" or key == "updated_at":
					self.__dict__[key] = datetime.fromisoformat(value)
				else:
					self.__dict__[key] = value
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)

	def __str__(self):
		"""To return a string value"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""To update to current time"""
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		"""returna a dictionary containing all keys and values of __dict__ of the instance"""
		dict_copy = self.__dict__.copy()
		dict_copy["__class__"] = self.__class__.__name__
		dict_copy["created_at"] = self.created_at.isoformat()
		dict_copy["updated_at"] = self.updated_at.isoformat()
		return dict_copy
