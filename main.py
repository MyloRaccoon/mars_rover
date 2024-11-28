from rover import Rover
from planet import Planet
from position import Position
from obstacle import Obstacle
from api.remote import Remote

if __name__ == '__main__':

	planet: Planet = Planet(100, 100, Obstacle(Position(1,0)), Obstacle(Position(10,10)), Obstacle(Position(15,13)))
	rover: Rover = Rover(Position(0, 0), planet)
	remote: Remote = Remote(rover)

	answer = ""
	while True:
		print(rover)
		answer = input()
		remote.execute(answer)