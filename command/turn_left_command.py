from command.command import Command

class TurnLeftCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_left()