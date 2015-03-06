from random import randint, sample

R = lambda x: int(round(x)) # wrapper for rounding

class GenerateMap(object):
	"""class which is responsible for the world generation"""
	def __init__(self, x, y):
		super(GenerateMap, self).__init__()
		self.size = (x, y)
		self.map = [[0]*y for i in range(x)]
		self.split(0, self.size[0], 0, self.size[1])

	def split(self, xlo, xhi, ylo, yhi):
		# absolutely failed
		if min(xhi-xlo, yhi-ylo) < 3:
			return None
			
		# generate room in splitted space
		if (xhi-xlo) * (yhi-ylo) <= 30:
			# random split
			values = sample(range(xlo, xhi), 3) # 3 adjust size
			xlo, xhi = min(values), max(values)
			values = sample(range(ylo, yhi), 3) # 3 adjust size
			ylo, yhi = min(values), max(values)

			# set room
			self.set_room(xlo, xhi, ylo, yhi)

			# return for futher calculations
			return (xlo, xhi, ylo, yhi)
			
		if True or randint(0, 1):
			# x split value
			# it is between xlo and xhi but not too close (10%) of each ending
			var = R(xlo + (xhi-xlo)*0.1 + randint(0, xhi-xlo)*0.8)

			# recursive room generation
			a = self.split(xlo, var, ylo, yhi)
			b = self.split(var+1, xhi, ylo, yhi)

			# check if one did not return a room
			if not a:
				return b

			if not b:
				return a

			# a, b yield rooms




	def set_room(self, xlo, xhi, ylo, yhi):
		for x in range(xhi-xlo):
			for y in range(yhi-ylo):
				self.map[xlo+x][ylo+y] = 1


if __name__ == '__main__':
	import pprint;
	gen = GenerateMap(10, 10)
	pprint.pprint(gen.map)

