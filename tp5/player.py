class Player(object):
	"""docstring for Player"""
	def __init__(self, gen, points = 0):
		super(Player, self).__init__()
		self.strategy = gen[2:6]
		self.lastGame = gen[0:2]
		self.points = points

	def __repr__(self):
		return str((self.strategy, self.lastGame, self.points))

	def __str__(self):
		return self.__repr__()
		
	def play(self):
		if self.lastGame == ('A', 'A'):
			return self.strategy[0]
		elif self.lastGame == ('A', 'N'):
			return self.strategy[1]
		elif self.lastGame == ('N', 'A'):
			return self.strategy[2]
		elif self.lastGame == ('N', 'N'):
			return self.strategy[3]

	def reset(self):
		self.points = 0