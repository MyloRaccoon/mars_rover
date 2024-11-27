from command import Command

class Invoker:

	def __init__(self):
		self.commands: dict[str, Command] = {}

	def add_command(self, entry: str, command: Command):
		self.commands[entry] = command

	def execute(self, entry: str):
		if entry in self.commands.keys():
			self.commands[entry].execute()
		else:
			raise Exception(f'Command "{entry}" does not exist.')
