class Bag(object):
	def __init__(self, inside = [], maxSize):
		super(Bag, self).__init__()
		self._inside = inside
		self._maxSize = maxSize
	
	def getSize(self):
		size = 0
		for aux in self._inside:
			size = size + aux.getVolume()
		return size

	def canAdd(self, item):
	 	return False if self.getSize() + item.getVolume > self._maxSize: else return True

	def add(self, item):
		self._inside.append(item)

	def getTotalValue(self):
		total = 0
		for aux in self._inside:
			total = total + aux.getValue()
		return total