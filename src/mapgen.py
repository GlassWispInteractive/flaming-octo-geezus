from random import randint, sample, choice

R = lambda x: int(round(x)) # wrapper for rounding


class GenerateMap(object):
	"""class which is responsible for the world generation"""
	def __init__(self, x, y):
		super(GenerateMap, self).__init__()
		self.x, self.y = (x, y)
		self.map = [[0]*self.y for i in range(self.x)]
		self.split(0, self.x, 0, self.y, 4)

	def split(self, xlo, xhi, ylo, yhi, iteration):
		# too small
		if min(xhi-xlo, yhi-ylo) < 4:
			return
		
		
			
		# generate room in splitted space
		if (xhi-xlo) * (yhi-ylo) <= 30 or iteration == 0:
			temp = R((xhi-xlo)*0.3)
			xlo += randint(0, temp) + 0
			temp = R((xhi-xlo)*0.3)
			xhi -= randint(0, temp) + 0

			temp = R((yhi-ylo)*0.3)
			ylo += randint(0, temp) + 0
			temp = R((yhi-ylo)*0.3)
			yhi -= randint(0, temp) + 0


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
			var = R(xlo + (xhi-xlo)*0.45 + randint(0, R((xhi-xlo)*0.1)) )
			
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
			var = R(ylo + (yhi-ylo)*0.45 + randint(0, R((yhi-ylo)*0.1)) )
			
			print "ys", var, ylo, yhi
			# recursive room generation
			a = self.split(xlo, xhi, ylo, var, iteration-1)
			b = self.split(xlo, xhi, var, yhi, iteration-1)
				



	def set_room(self, xlo, xhi, ylo, yhi):
		num = randint(10,100)
		for x in range(xhi-xlo):
			for y in range(yhi-ylo):
				self.map[xlo+x][ylo+y] = 1





class GenerateMapTetris(object):
	"""class which is responsible for the world generation"""
	def __init__(self, x, y):
		super(GenerateMap, self).__init__()
		self.x, self.y = (x, y)
		self.map = [[0]*self.y for i in range(self.x)]
		# self.gen_rooms(0, self.x, 0, self.y, 4)
		self.gen_rooms(4, 7, 5)

	def gen_rooms(self, lo, hi, count):
		room = self.rand_room(lo, hi)
		xoff, yoff = R((self.x-room[0])/2), R((self.y-room[1])/2)
		self.set_room(xoff, xoff + room[0], yoff, yoff + room[1])

		for _ in range(count): # room
			room = self.rand_room(lo, hi)

			for _1 in sample(range(4), 4):
				# rotate array
				self.map = [list(t) for t in zip(*self.map[::-1])]
				# print self.map

				limit = len(self.map)

				depth = [0] * limit
				# check maximum depth
				for z in range(limit):
					for d in range(len(self.map[0])):
						if self.map[z][d]:
							break
						depth[z] = d
					# print depth[z]

				# calc deepest size
				val, ind = min(depth[:room[0]]), 0
				for k in range(limit-room[0]+1):
					if min(depth[k:k+room[0]]) > val:
						ind = k

				if depth > room[0]:
					# print ind, ind + room[0], val - room[1], val
					self.set_room(ind, ind + room[0], val - room[1], val)
					break
				# print ind, depth[ind]


	def rand_room(self, lo, hi):
		return randint(lo, hi), randint(lo, hi)


	def set_room(self, xlo, xhi, ylo, yhi):
		print xlo, xhi, ylo, yhi

		for x in range(xhi-xlo):
			for y in range(yhi-ylo):
				self.map[xlo+x][ylo+y] = 1


	def rotate(self, x, y, c):
		"MAGIC MAGIC MAGIC MAGIC MAGIC MAGIC <3"
		if c == 0:
			return x,y
		elif c == 1:
			return self.x - y, x
		elif c == 2:
			return self.x - x, self.y - y
		elif c == 3:
			return y, self.y - x

		
if __name__ == '__main__':
	import pprint;
	gen = GenerateMap()
	pprint.pprint(gen.map)

