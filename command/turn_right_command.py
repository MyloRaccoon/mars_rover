from command.command import Command

class TurnRightCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_right()