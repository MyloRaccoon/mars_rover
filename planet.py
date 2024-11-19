from object import Object

class Planet:

	def __init__(self, width: int, height: int, *objects: Object):
		self.width: int = width
		self.height: int = height
		self.objects: list[Object] = []
		for object in objects:
			self.objects.append(object)

	def add_objects(self, *objects: Object):
		for object in objects:
			self.objects.append(object)