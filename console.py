#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
	"""Console"""
	prompt = "(hbnb) "

	def do_quit(self, line):
		"""Exit Console"""
		return True

	def do_EOF(self, line):
		"""Exit Console"""
		return True

	def emptyline(self):
		pass

if __name__ == "__main__":
	HBNBCommand().cmdloop()
