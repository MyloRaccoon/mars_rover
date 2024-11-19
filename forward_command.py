from command import Command

class ForwardCommand(Command):

	def __init__(self, rover):
		self.rover = rover

	def execute(self):
		self.rover.forward()