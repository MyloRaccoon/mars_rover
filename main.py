from rover import Rover
from planet import Planet


if __name__ == '__main__':


	planet: Planet = Planet(100, 100)
	rover: Rover = Rover(0, 0, planet)

	answer = ""
	while answer != 'e':
		print(rover)
		answer = input()
		rover.execute(answer)