from time import strftime
from lib import chrToString, binToDec

class logger(object):
	'''This object will manage all the logs functions'''

	def __init__(self):
		'''initialize the log file'''
		super(logger, self).__init__()
		self.fname = 'logs/' + (strftime("%x") + strftime("%X")).replace('/', '').replace(':', '') + '.log'

	def startReport(self, coChance, mChance, iterations, reportEach):
		'''Writes log header'''
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
		'''Writes log footer'''
		self.log.write('\n\nEnded on:\t' + strftime("%x") + '\tat:\t' + 
			strftime("%X") + '\n')
		self._close()
		
	def reportLine(self, popCount, ofValues, ffValues):
		'''Writes a single line of the log responding to one single population'''
		ofAvg = sum(ofValues) / len(ofValues)
		ofMax = max(ofValues)
		ofMin = min(ofValues)

		self.log.write(str(popCount))
		self.log.write(
			'\t' + str(ofMax).replace('.', ',') + 
			'\t' + str(ofMin).replace('.', ',') + 
			'\t' + str(ofAvg).replace('.', ',') + '\n')

	def reportChampion(self, champion, championObj, championPop ):
		'''Writes the information of the best Chromosome of the running'''
		self.log.write('Best Chromosome:\t' + chrToString(champion) + 
			'\nDecimal Value:\t' + str(int(chrToString(champion), 2)) + 
			'\nObjetive:\t' + str(championObj) +
			'\nPopulation:\t' + str(championPop))

	def _open(self):
		'''Open the logs file on append mode'''
		self.log = open(self.fname, 'a')

	def _close(self):
		'''Close the logs file'''
		self.log.close()