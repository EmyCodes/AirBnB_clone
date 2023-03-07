#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
	"""Console"""
	prompt = "(hbnb) "
	__classes = ["BaseModel", 
			"User",
			"Place",
			"State",
			"City",
			"Amenity",
			"Review"
		]

	def do_quit(self, line):
		"""to Exit Console
		"""
		return True

	def do_EOF(self, line):
		"""to Exit Console
		"""
		return True

	def emptyline(self):
		"""Passes an emply line instead of repeating previous command
		"""
		pass

	def do_create(self, arg):
		"""Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
		"""
		args = arg.split()
		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in self.__classes:
			print("** class doesn't exist **")
		else:
			new_object = eval(f"{args[0]}")()
			print(new_object.id)
<<<<<<< HEAD
<<<<<<< HEAD
=======
		
=======
		storage.save()	
>>>>>>> emycodes
	def do_show(self, arg):
		"""Prints the string representation of an instance based on the class name and id
		"""
		args = arg.split()
		#no_cls_name = eval(f"{args[0]")())

		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in self.__classes:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found **")
		else:
			print(storage.all()[f"{args[0]}.{args[1]}"])

	def do_destroy(self, arg):
		""" Deletes an instance based on the class name and id (save the change into the JSON file)

		"""
		args = arg.split()

		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in self.__classes:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found **")
		else:
			del storage.all()[f"{args[0]}.{args[1]}"]
		storage.save()
		
	def do_all(self, arg):
		"""Prints all string representation of all instances based or not on the class name.
		"""
		args = arg.split()
			
		if len(args) == 0:
			print([str(v) for v in storage.all().values()])
		elif args[0] not in self.__classes:
			print("** class doesn't exist **")
		else:
			print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])

	def do_update(self, arg):
		"""Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
		"""
		args = arg.split()

		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in self.__classes:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
		elif f"{args[0]}.{args[1]}" not in storage.all():
			print("** no instance found **")
		elif len(args) == 2:
			print("** attribute name missing **")
		elif len(args) == 3:
			print("** value missing **")
		else:
			obj_name = args[0]
			obj_id = args[1]

			obj_key = f"{obj_name}.{obj_id}"
			obj = storage.all()[obj_key]

			attr_name = args[2]
			attr_value = args[3].replace('"', "").replace("'", "")

			#print("-----------")
			#print()
			#print(obj)
			# if attr_value == "'" or attr_value == '"':
			#	attr_value = attr_value[1:-1]
				# attr_value = attr_value.strip('"').strip("'")
			#	print(attr_value)	

			if hasattr(obj, attr_name):
				type_ = type(getattr(obj, attr_name))
				if type_ in [str, int, float]:
					attr_value = type_(attr_value)
					setattr(obj, attr_name, attr_value)
			else:
				setattr(obj, attr_name, attr_value)
			
		storage.save()

	def default(self, arg):
		"""default
		"""
		args = arg.split(".")
		if args[0] in self.__classes:
			if args[1] == "all()":
				self.do_all(args[0])
			elif args[1] == "count()":
				list_ = [v for k, v in storage.all().items() if k.startswith(args[0])]
				print(len(list_))
			elif args[1].startswith("show"):
				split_ = args[1].split('"')
				id_ = split_[1]
				self.do_show(f"{args[0]} {id_}")
			elif args[1].startswith("destroy"):
				split_ = args[1].split('"')
				id_ = split_[1]
				self.do_destroy(f"{args[0]} {id_}")
<<<<<<< HEAD

>>>>>>> emycodes
=======
			elif args[1].startswith("update"):
				if '{' or '}' in args[1]:
					split_ = args[1].split("(")
					split_ = split_[1].split(", {")
					id_ = split_[0].strip('"')
					dict_ = "{" + split_[1].strip(')')
					dict_ = eval(dict_)
					for k, v in dict_.items():
						#print(f"{k} = {v}")
						self.do_update(f"{args[0]} {id_} {k} {v}")
				else:
					print("I don't have a dictionary")
					id_ = split_[0]
					replace_ = args[1].replace('"', "")
					split_ = replace_.split("(")
					split_ = split_[1].strip(")").split(", ")
					attr_name = split_[1]
					attr_value = split_[2]
					#print(id_)
					#print(attr_name)
					#print(attr_value)
					self.do_update(f"{args[0]} {id_} {attr_name} {attr_value}")
				
>>>>>>> emycodes

if __name__ == "__main__":
	HBNBCommand().cmdloop()

