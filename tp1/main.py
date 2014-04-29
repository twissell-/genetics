from lib import newPopulation, objetiveFunc, fitness, crossover, mutation
from logger import logger

population = newPopulation(10, 30)
coChance = 0.75
mChance = 0.9
iterations = 200000
reportEach = iterations / 20

logger = logger()
logger.startReport(coChance, mChance, iterations, reportEach)

for x in xrange(0, iterations):
	if(x % reportEach == 0):
		logger.reportLine(x, objetiveFunc(population), fitness(population))
		population = mutation(crossover(population, coChance), mChance)


logger.endReport()
