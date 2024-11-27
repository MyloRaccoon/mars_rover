from object import Object
from direction import Direction
from position import Position
from invoker import Invoker
from forward_command import ForwardCommand
from backward_command import BackwardCommand
from turn_left_command import TurnLeftCommand
from turn_right_command import TurnRightCommand
from quit_command import QuitCommand
from planet import Planet

class Rover(Object):
    def __init__(self, position: Position, planet: Planet):
        super().__init__(position)
        self.direction: Direction = Direction.NORTH
        self.remote: Invoker = Invoker()
        self.set_commands()
        self.planet: Planet = planet

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
        new_position: Position = self.position.copy()

        match (self.direction):
            case Direction.NORTH:
                new_position.y += 1
            case Direction.WEST:
                new_position.x += -1
            case Direction.SOUTH:
                new_position.y += -1
            case Direction.EAST:
                new_position.x += 1

        self.position = new_position.copy()

        self.wrap()

    def wrap(self):
        if self.position.x < 0:
            self.position.x = self.planet.width
        elif self.position.x > self.planet.width:
            self.position.x = 0

        if self.position.y < 0 :
            self.position.y = self.planet.height
        elif self.position.y > self.planet.height:
            self.position.y = 0

    def backward(self):
        match (self.direction):
            case Direction.NORTH:
                self.position.x += -1
            case Direction.WEST:
                self.position.y += 1
            case Direction.SOUTH:
                self.position.x += 1
            case Direction.EAST:
                self.position.y += -1

    def __str__(self) -> str:
        return f"Rover at {self.position} | looking at {self.direction}"