class Vector:
	def __init__(self, x, y):
		self.x = x 
		self.y = y 

	def __repr__(self):
		return f'{self.__class__} ({self.x}, {self.y})'

# >>> from vector import *
# >>> v = Vector(5, 3)
# >>> dir(v)
# >>> v.__dict__
# >>> type(v.__dict__)
# >>> v.__dict__['x']
# >>> v.__dict__['x'] = 10
# >>> v
# >>> del v.__dict__['x']
# >>> v.x
# >>> 'x' in v.__dict__
# >>> 'y' in v.__dict__
# >>> v.__dict__['z'] = 13
# >>> v.z

# >>> getattr(v, 'y')
# >>> hasattr(v, 'x')
# >>> delattr(v, 'z')
# >>> setattr(v, 'x', 9)
# >>> v.x
