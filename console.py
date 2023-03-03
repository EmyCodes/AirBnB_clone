#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
	"""Console"""
	prompt = "(hbnb) "

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

if __name__ == "__main__":
	HBNBCommand().cmdloop()

