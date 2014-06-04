class Item(object):
	def __init__(self, volume, value):
		super(Item, self).__init__()
		self._volume = volume
		self._value = value

	def getValue(self):
		return self._value

	def getVolume(self):
		return self._volume
		