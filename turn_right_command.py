from command import Command
from rover import Rover

class TurnRightCommand(Command):
    def __init__(self, rover : Rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_right()