class Item(object):
	def __init__(self, volume, value):
		self._volume = volume
		self._value = value
		self._coef = self._value / self._volume

	def __str__(self):
		return "(%d, %d)" % (self._volume, self._value)

	def __repr__(self):
		return self.__str__()
		
	def getVolume(self):
		return self._volume

	def getValue(self):
		return self._value

	def getCoef(self):
		return self._coef