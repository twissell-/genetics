from lib import *
from data import *

population = newPopulation(50, 23, 23)
coChance = .76
mChance = .05
iterations = 1000000
reportEach = iterations / 1
champion = population[0]
championObjFunc = oneObjFunc(champion)
championPop = 0

print('[i]: Running...')

for x in range(0, iterations):
	if x % 100 == 0:
		print('[i]: %.1f' % (x * 100 / iterations)) 
	localChampion = championship(population)
	if oneObjFunc(localChampion) > oneObjFunc(champion):
		champion = localChampion
		championObjFunc = oneObjFunc(champion)
		championPop = x
	population = mutation(crossover(population, coChance), mChance)

print('[i]: Done!')
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
