from object import Object
from direction import Direction

class Rover(Object):
    def __init__(self, x, y):
        super.__init__(self, x, y)
        self.direction = Direction.NORTH

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