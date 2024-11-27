from object import Object
from position import Position

class Planet:

	def __init__(self, width: int, height: int, *objects: Object):
		self.width: int = width
		self.height: int = height
		self.objects: dict[str, Object] = {}
		for object in objects:
			self.objects[object.position.__str__()] = object

	def add_objects(self, *objects: Object):
		for object in objects:
			self.objects.append(object)

	def get_object_at(self, position: Position) -> Object:
		if position.__str__() in self.objects:
			return self.objects[position.__str__()]