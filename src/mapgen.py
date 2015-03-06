from random import randint, sample, choice

R = lambda x: int(round(x)) # wrapper for rounding

class GenerateMap(object):
	"""class which is responsible for the world generation"""
	def __init__(self):
		super(GenerateMap, self).__init__()
		self.x, self.y = (300, 300)
		self.map = [[0]*self.y for i in range(self.x)]
		self.split(0, self.x, 0, self.y, 2)

	def split(self, xlo, xhi, ylo, yhi, iteration):
		# too small
		if min(xhi-xlo, yhi-ylo) < 3:
			return
		
		
			
		# generate room in splitted space
		if (xhi-xlo) * (yhi-ylo) <= 30 or iteration == 0:
			# values = sample(range(xlo, xhi), 2) # [randint(xlo, xhi) for _ in range(3)]
			# xlo, xhi = min(values), max(values)
			# values = sample(range(ylo, yhi), 2)
			# ylo, yhi = min(values), max(values)

			# set room
			self.set_room(xlo, xhi-1, ylo, yhi-1)

			# return for futher calculations
			return (xlo, xhi, ylo, yhi)
			
		if randint(0, 1):
			# x split value
			# it is between xlo and xhi but not too close (10%) of each ending
			var = R(xlo + 1 + randint(0, xhi-xlo-1))
			
			print "xs", var, xlo, xhi
			# recursive room generation
			a = self.split(xlo, var, ylo, yhi, iteration-1)
			b = self.split(var, xhi, ylo, yhi, iteration-1)

			# check if one did not return a room
			# if not a:
			# 	return b

			# if not b:
			# 	return a

			# # a, b yield rooms
			# # if a[3] > b[3]:
			# # 	a,b = b,a
			# rangea = set(range(a[0], a[1]+1))
			# rangeb = set(range(b[0], b[1]+1))
			
			# poss = rangea.intersection(rangeb)
			# if poss:
			# 	x = list(choice(poss))
			# 	ylo = a[3]
			# 	yhi = b[2]
			# 	self.set_room(x, x, ylo, yhi)
			# else:
			# 	print a, rangea
			# 	print b, rangeb
			# 	print "this means work"
		else:
			var = R(ylo + 1 + randint(0, yhi-ylo-1))
			
			print "ys", var, ylo, yhi
			# recursive room generation
			a = self.split(xlo, xhi, ylo, var, iteration-1)
			b = self.split(xlo, xhi, var, yhi, iteration-1)
				



	def set_room(self, xlo, xhi, ylo, yhi):
		num = randint(10,100)
		for x in range(xhi-xlo):
			for y in range(yhi-ylo):
				self.map[xlo+x][ylo+y] = 1


if __name__ == '__main__':
	import pprint;
	gen = GenerateMap()
	pprint.pprint(gen.map)

