#!/usr/bin/python3
"""
Base model.
"""
import uuid
from datetime import datetime

class BaseModel:
	"""
	base model class.
	"""
	def __init__(self, name=None, my_number= None, updated_at=None, id=None, created_at=None):
    
		self.my_number = my_number
		self.name = name
		self.updated_at = datetime.now()
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()

	def __str__(self):
        
		return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

	
	def save(self):
	"""
	saves new date.
	"""
		self.updated_at = datetime.now()

	
	def to_dict(self):
	"""
	returns dict representaion.
	"""
		return {
			"my_number": self.my_number,
			"name": self.name,
			"__class__": self.__class__.__name__,
			"updated_at": self.updated_at.isoformat(),
			"id": self.id,
			"created_at": self.created_at.isoformat()
		}
		
