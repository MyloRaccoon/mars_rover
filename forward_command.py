from command import Command
from rover import Rover

class forwardCommand(Command):

	def __init__(self, rover: Rover):
		self.rover = rover

	def execute(self):
		rover.forward()