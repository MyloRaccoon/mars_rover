from rover import Rover
from planet import Planet


if __name__ == '__main__':

	rover: Rover = Rover(0, 0)

	planet: Planet = Planet(100, 100)

	answer = ""
	while answer != 'e':
		print(rover)
		answer = input()
		rover.execute(answer)