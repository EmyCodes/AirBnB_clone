#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

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

if __name__ == "__main__":
	HBNBCommand().cmdloop()

