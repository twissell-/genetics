class Item(object):
	def __init__(self, volume, value, id = 0):
		self._volume = volume
		self._value = value
		self._id = id
		self._coef = self._value / self._volume

	def __str__(self):
		return "%s:(%d, %d)" % (self._id, self._volume, self._value)

	def __repr__(self):
		return self.__str__()
		
	def getVolume(self):
		return self._volume

	def getValue(self):
		return self._value

	def getCoef(self):
		return self._coef