from lib import *

population = newPopulation(50, 23, 23)
coChance = 0.75
mChance = 0.05
iterations = 10000
reportEach = iterations / 1
champion = population[0]
championObjFunc = oneObjFunc(champion)
championPop = 0

for x in range(0, iterations):
	# if(x % reportEach == 0):
	localChampion = championship(population)
	if oneObjFunc(localChampion) > oneObjFunc(champion):
		champion = localChampion
		championObjFunc = oneObjFunc(champion)
		championPop = x
	population = mutation(crossover(population, coChance), mChance)
print(champion)
print(oneObjFunc(champion))
