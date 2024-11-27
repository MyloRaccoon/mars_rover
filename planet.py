from object import Object
from position import Position

class Planet:

	def __init__(self, width: int, height: int, *objects: Object):
		self.width: int = width
		self.height: int = height
		self.objects: dict[str, Object] = {}
		for object in objects:
			self.add_object(object)

	def add_objects(self, *objects: Object):
		for object in objects:
			self.add_object(object)

	def add_object(self, object: Object):
		if object.position.__str__() in self.objects.keys():
			print(f"/!\\ can't add object {object} to planet {self} : there's already an object at position {object.position}.")
		elif object.position.x < 0 or object.position.x > self.width or object.position.y < 0 or object.position.y > self.height:
			print(f"/!\\ can't add object {object} to planet {self} : position out of planet's range")
		else:
			self.objects[object.position.__str__()] = object

	def get_object_at(self, position: Position) -> Object:
		if position.__str__() in self.objects.keys():
			return self.objects[position.__str__()]