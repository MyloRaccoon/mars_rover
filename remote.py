from invoker import Invoker
from forward_command import ForwardCommand
from backward_command import BackwardCommand
from turn_left_command import TurnLeftCommand
from turn_right_command import TurnRightCommand
from quit_command import QuitCommand
from rover import Rover

class Remote(Invoker):

	def __init__(self, rover: Rover):
		super().__init__()
		self.add_command('f', ForwardCommand(rover))
		self.add_command('b', BackwardCommand(rover))
		self.add_command('r', TurnRightCommand(rover))
		self.add_command('l', TurnLeftCommand(rover))
		self.add_command('e', QuitCommand())