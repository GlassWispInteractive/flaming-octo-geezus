
class Pill(object):
	""" Items - Pills """
	def __init__(self, x, y, type):
		super(Pill, self).__init__()
		self.x = x
		self.y = y
		self.hp = 1 if type == 1 else 10
