from lib import *
from data import *

population = newPopulation(50, 23, 23)
coChance = .75
mChance = .05
iterations = 1000000
reportEach = iterations / 1
champion = population[0]
championObjFunc = oneObjFunc(champion)
championPop = 0

print('Running...')

for x in range(0, iterations):
	# if(x % reportEach == 0):
	localChampion = championship(population)
	if oneObjFunc(localChampion) > oneObjFunc(champion):
		champion = localChampion
		championObjFunc = oneObjFunc(champion)
		championPop = x
	population = mutation(crossover(population, coChance), mChance)

print('Done!')
print('''
Final Result:
=============
''')
print('- Iterations: %d' % iterations)
print('- Cross-over Chance: %.2f' % coChance)
print('- Mutation Chance: %.2f' % mChance)
print('- Distance: %d' % abs(oneObjFunc(champion)))
print('- Route:')
c = 0
aux = []
for x in champion:
	c += 1
	aux.append('%d. ' % c + cities[x])
print(str(aux).replace('[', '').replace(']', '').replace('\'', ''))
