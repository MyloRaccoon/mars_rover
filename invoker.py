from rover import Rover
from forward_command import ForwardCommand
from backward_command import BackwardCommand
from turn_left_command import TurnLeftCommand
from turn_right_command import TurnRightCommand

class Invoker:

	def __init__(self):
		self.commands: dict[str, Command] = {}

	def add_command(self, entry: str, command: Command):
		self.commands[entry] = command

	def execute(self, entry):
		if entry in self.commands.keys():
			self.commands[entry].execute()
		else:
			raise Exception(f'Command "{entry}" does not exist.')
