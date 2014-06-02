from lib import *
from logger import logger

population = newPopulation(10, 30)
coChance = 0.75
mChance = 0.05
iterations = 1000
reportEach = iterations / 20
champion = population[0]
championObjFunc = oneObjFunc(champion)
championPop = 0

print 'Running...'

logger = logger()
logger.startReport(coChance, mChance, iterations, reportEach)

for x in xrange(0, iterations):
	# if(x % reportEach == 0):
	logger.reportLine(x, objetiveFunc(population), fitness(population))
	localChampion = championship(population)
	if int(chrToString(localChampion), 2) > int(chrToString(champion), 2):
		champion = localChampion
		championObjFunc = oneObjFunc(champion)
		championPop = x
	population = mutation(crossover(population, coChance), mChance)

logger.reportChampion(champion, championObjFunc, championPop)
logger.endReport()
print 'Done!'