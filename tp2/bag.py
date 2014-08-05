class Bag(object):
	def __init__(self, inside = []):
		super(Bag, self).__init__()
		self._inside = inside

	def __str__(self):
		return "Tvol: %d Tval: %d" % (self.getSize(), self.getTotalValue()) + '\n' + str(self._inside)

	def __repr__(self):
		return self.__str__()
	
	def getSize(self):
		size = 0
		for aux in self._inside:
			size = size + aux.getVolume()
		return size

	def add(self, item):
		self._inside.append(item)

	def getTotalValue(self):
		total = 0
		for aux in self._inside:
			total = total + aux.getValue()
		return total