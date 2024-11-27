from object import Object
from position import Position

class Obstacle(Object):
    def __init__(self, position: Position):
        super().__init__(position)
