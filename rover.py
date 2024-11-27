from object import Object
from direction import Direction
from invoker import Invoker
from forward_command import ForwardCommand
from backward_command import BackwardCommand
from turn_left_command import TurnLeftCommand
from turn_right_command import TurnRightCommand
from quit_command import QuitCommand
from planet import Planet

class Rover(Object):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.direction: Direction = Direction.NORTH
        self.remote: Invoker = Invoker()
        self.set_commands()

    def set_commands(self):
        self.remote.add_command('f', ForwardCommand(self))
        self.remote.add_command('b', BackwardCommand(self))
        self.remote.add_command('r', TurnRightCommand(self))
        self.remote.add_command('l', TurnLeftCommand(self))
        self.remote.add_command('e', QuitCommand())

    def execute(self, entry: str):
        for c in entry:
            try:
                self.remote.execute(c)
            except Exception as e:
                print(f"/!\\ command {c} ignored ({e})")


    def turn_left(self):
        match(self.direction):
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.WEST:
                self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.NORTH


    def turn_right(self):
        match(self.direction):
            case Direction.NORTH:
                self.direction = Direction.EAST
            case Direction.WEST:
                self.direction = Direction.NORTH
            case Direction.SOUTH:
                self.direction = Direction.WEST
            case Direction.EAST:
                self.direction = Direction.SOUTH

    def forward(self):
        match (self.direction):
            case Direction.NORTH:
                self.x += 1
            case Direction.WEST:
                self.y += -1
            case Direction.SOUTH:
                self.x += -1
            case Direction.EAST:
                self.y += 1

    def backward(self):
        match (self.direction):
            case Direction.NORTH:
                self.x += -1
            case Direction.WEST:
                self.y += 1
            case Direction.SOUTH:
                self.x += 1
            case Direction.EAST:
                self.y += -1

    def __str__(self) -> str:
        return f"Rover at ({self.x},{self.y}) | looking at {self.direction}"