#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
	"""Console"""
	prompt = "(hbnb) "
	__classes = ["BaseModel"]

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


if __name__ == "__main__":
	HBNBCommand().cmdloop()

