from time import strftime
from lib import chrToString, binToDec

class logger(object):
	'''This object will manage all the logs functions'''

	def __init__(self):
		super(logger, self).__init__()
		self.fname = 'logs/' + (strftime("%x") + strftime("%X")).replace('/', '').replace(':', '') + '.ods'

	def startReport(self, coChance, mChance, iterations, reportEach):
		self._open()
		self.log.write('Genetic Algorithm Log\n' +
			'Started on:\t' + strftime("%x") + '\tat:\t' + strftime("%X") + '\n' +
			'Cross-Over chance:\t' + str(coChance) + '\t' + 
			'Mutation chance:\t' + str(mChance) + '\n' + 
			'Iterations:\t' + str(iterations) + '\t' + 
			'Reporting each:\t' + str(reportEach) + ' iterations\n')
		self.log.write('\n')
		self.log.write('"Population"\t"Obj. Max"\t"Obj. Min"\t"Obj. Avg"\n')

	def endReport(self):
		self._writeFooter()
		self._close()
		
	def reportLine(self, popCount, ofValues, ffValues):
		ofAvg = sum(ofValues) / len(ofValues)
		ofMax = max(ofValues)
		ofMin = min(ofValues)

		self.log.write(str(popCount))
		self.log.write(
			'\t' + str(ofMax).replace('.', ',') + 
			'\t' + str(ofMin).replace('.', ',') + 
			'\t' + str(ofAvg).replace('.', ',') + '\n')

	def reportChampion(self, champion, championObj, championPop ):
		self.log.write('Best Chromosome:\t' + chrToString(champion) + 
			'\nDecimal Value:\t' + str(int(chrToString(champion), 2)) + 
			'\nObjetive:\t' + str(championObj) +
			'\nPopulation:\t' + str(championPop))

	def _open(self):
		self.log = open(self.fname, 'a')

	def _close(self):
		self.log.close()

	def _writeFooter(self):
		self.log.write('\n\nEnded on:\t' + strftime("%x") + '\tat:\t' + 
			strftime("%X") + '\n')

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