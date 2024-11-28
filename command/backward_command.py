from command.command import Command

class BackwardCommand(Command):

	def __init__(self, rover):
		self.rover = rover

	def execute(self):
		self.rover.backward()