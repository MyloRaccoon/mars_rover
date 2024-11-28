from command.command import Command
from rover import Rover
class TurnLeftCommand(Command):
    def __init__(self, rover : Rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_left()