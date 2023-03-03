#!/usr/bin/python3
import cmd

class HBNB(cmd.Cmd):
	"""Console"""
	prompt = "(hbnb) "

	def do_quit(self):
		"""Exit Console"""
		return True

	def do_EOF(self):
		"""Exit Console"""
		return True

	def emptyline(self):
		pass

if __name__ == "__main__":
	HBNBCommand().cmdloop()
