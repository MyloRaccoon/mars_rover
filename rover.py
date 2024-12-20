from object import Object
from direction import Direction
from position import Position
from planet import Planet
from obstacle_encounter_exception import ObstacleEncounterException

class Rover(Object):
    def __init__(self, position: Position, planet: Planet):
        super().__init__(position)
        self.direction: Direction = Direction.NORTH
        self.planet: Planet = planet


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

        if self.planet.get_obstacle_at(new_position) is None:
            self.position = new_position.copy()
            self.wrap()
        else:
            raise ObstacleEncounterException(f"/!\\ Can't move to {new_position} because there is already an object here.")

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
        new_position: Position = self.position.copy()

        match (self.direction):
            case Direction.NORTH:
                new_position.y += -1
            case Direction.WEST:
                new_position.x += 1
            case Direction.SOUTH:
                new_position.y += 1
            case Direction.EAST:
                new_position.x += -1

        if self.planet.get_obstacle_at(new_position) is None:
            self.position = new_position.copy()
            self.wrap()
        else:
            raise ObstacleEncounterException(f"/!\\ Can't move to {new_position} because there is already an object here.")

    def __str__(self) -> str:
        return f"Rover at {self.position} | looking at {self.direction}"