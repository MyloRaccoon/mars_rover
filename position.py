class Position:

	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def copy(self):
		return Position(self.x, self.y)

	def __str__(self) -> str:
		return f"({self.x}, {self.y})"

	def __eq__(self, other):
		return (self.x == other.x and self.y == self.y)