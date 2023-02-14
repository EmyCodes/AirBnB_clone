#!/usr/bin/python3
from datetime import datetime

class BaseModel():
	"""Defining a Parent class"""

	def __init__(self):
		"""Initialize init function"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__():
		"""Function that display current class name and id and dictionary"""
		return f"[{self.__class__.__name___}] ({self.id}) {self.__dict__}"

	def save(self):
		"""Function that saves"""
		self.updated_at - datetime.now()

	def to_dict(self):
		pass


