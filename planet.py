from obstacle import Obstacle
from position import Position

class Planet:

	def __init__(self, width: int, height: int, *obstacles: Obstacle):
		self.width: int = width
		self.height: int = height
		self.obstacles: dict[str, Obstacle] = {}
		for obstacle in obstacles:
			self.add_obstacle(obstacle)

	def add_obstacles(self, *obstacles: Obstacle):
		for obstacle in obstacles:
			self.add_obstacle(obstacle)

	def add_obstacle(self, obstacle: Obstacle):
		if obstacle.position.__str__() in self.obstacles.keys():
			print(f"/!\\ can't add obstacle {obstacle} to planet {self} : there's already an obstacle at position {obstacle.position}.")
		elif obstacle.position.x < 0 or obstacle.position.x > self.width or obstacle.position.y < 0 or obstacle.position.y > self.height:
			print(f"/!\\ can't add obstacle {obstacle} to planet {self} : position out of planet's range")
		else:
			self.obstacles[obstacle.position.__str__()] = obstacle

	def get_obstacle_at(self, position: Position) -> Obstacle | None:
		if position.__str__() in self.obstacles.keys():
			return self.obstacles[position.__str__()]
		return None