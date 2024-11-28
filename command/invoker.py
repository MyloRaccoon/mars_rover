from command.command import Command
from abc import abstractmethod
class Invoker:

	def __init__(self):
		self.commands: dict[str, Command] = {}
		self.log: list[Command] = []

	def add_command(self, entry: str, command: Command):
		self.commands[entry] = command

	def execute(self, entry: str):
		for command_bracket in entry:
			if command_bracket in self.commands.keys():
				try:
					command = self.commands[command_bracket]
					command.execute()
					self.log.append(command)
				except Exception as e:
					self.handle_execute_exception(e)
					break
			else:
				raise Exception(f'Command "{command_bracket}" does not exist.')
	@abstractmethod
	def handle_execute_exception(self, exception: Exception):
		pass
		
