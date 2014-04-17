from time import strftime
from lib import chrToString

class logger(object):
	'''This object will manage all the logs functions'''

	def __init__(self):
		super(logger, self).__init__()
		self.fname = (strftime("%x") + strftime("%X")).replace('/', '').replace(':', '') + '.md'
		
	def open(self):
		self.log = open(self.fname, 'a')

	def close(self):
		self.log.close()

	def writeHeader(self):
		self.log.write('Genetic Algorithm Log\n')
		self.log.write('---\n\n')
		self.log.write('~~~\n')
		self.log.write('Started on: ' + strftime("%x"))
		self.log.write(' at ' + strftime("%X") + '\n')
		self.log.write('~~~\n\n')
		self.log.write('---\n')

	def writeReportHead(self):
		self.log.write('|Population|Obj. Sum|Obj. Avg|Obj. Max|Fit. Sum|Fit. Avg|Fit. Max|\n')
		self.log.write('|---|---|---|---|---|---|---|\n')

	def writeReportLine(self, popCount, ofValues, ffValues):
		ofSum = sum(ofValues)
		ofAvg = ofSum / len(ofValues)
		ofMax = max(ofValues)
		ffSum = sum(ffValues)
		ffAvg = ffSum / len(ffValues)
		ffMax = max(ffValues)

		self.log.write('|' + str(popCount))
		self.log.write('|' + str(ofSum) + '|' + str(ofAvg) + '|' + str(ofMax))
		self.log.write('|' + str(ffSum) + '|' + str(ffAvg) + '|' + str(ffMax) + '|\n')

	def writeFooter(self):
		self.log.write('---\n\n')
		self.log.write('~~~\n')
		self.log.write('Ended on: ' + strftime("%x"))
		self.log.write(' at ' + strftime("%X") + '\n')
		self.log.write('~~~\n\n')

	def writeSummary(self, popCount, ofValues, ffValues):
		'''Deprecated'''
		ofSum = sum(ofValues)
		ofAvg = ofSum / len(ofValues)
		ofMax = max(ofValues)
		ffSum = sum(ffValues)
		ffAvg = ffSum / len(ffValues)
		ffMax = max(ffValues)
		self.log.write('|' + str(popCount) + '|Objetive|Fitness|\n')
		self.log.write('|---|---|---|\n')
		self.log.write('|*Sum*|' + str(ofSum) + '|' + str(ffSum) + '|\n')
		self.log.write('|*Avg*|' + str(ofAvg) + '|' + str(ffAvg) + '|\n')
		self.log.write('|*Max*|' + str(ofMax) + '|' + str(ffMax) + '|\n')
		self.log.write('---\n')

	def writePopulation(self, population, popCount, popDec, ofValues, ffValues):
		'''Deprecated'''
		self.log.write('|' + str(popCount) + '|Chromesome|Decimal|Objetive|Fitness|\n')
		self.log.write('|---|---|---|---|---|\n')
		for x in xrange(0, len(population)):
			self.log.write('|' + str(x))
			self.log.write('|' + str(chrToString(population[x])))
			self.log.write('|' + str(popDec[x]))
			self.log.write('|' + str(ofValues[x]))
			self.log.write('|' + str(ffValues[x]) + '|\n')
		self.log.write('---\n')

# Usage Example
#
#from lib import newPopulation
#from logger import logger
#
#logger = logger()
#logger.open()
#logger.writeHeader()
#logger.writeReportHead()
#for x in xrange(1,1000):
#	popu = newPopulation(10, 30, 2)
#	logger.writeReportLine(x, objetiveFunc(popu, COEF), fitness(popu, COEF))
#logger.writeFooter()
#