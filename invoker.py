from command import Command

class Invoker:

	def __init__(self):
		self.commands: dict[str, Command] = {}

	def add_command(self, entry: str, command: Command):
		self.commands[entry] = command

	def execute(self, entry: str):
		for command in entry:
			if command in self.commands.keys():
				try:
					self.commands[command].execute()
				except Exception as e:
					self.handle_execute_exception(e)
			else:
				raise Exception(f'Command "{command}" does not exist.')

	def handle_execute_exception(self, exception: Exception):
		raise exception
