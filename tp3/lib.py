from random import randrange, random
from math import ceil
from data import distances, cities


def newPopulation(popSize, gens, ran = 2):
	'''This function returns a matrix of popSize x gens filled up with random 
	numbers from 0 to range - 1'''
	
	population = []

	for x in range(0, popSize):
		population.append([])
		for y in range(0, gens):
			while True:
				n = randrange(ran)
				if n not in population[x]:
					population[x].append(n)
					break
				
	return population

def getDistance(city, otherCity):
	'''Returns distances between city and otherCity It require the data package'''

	return distances[city][otherCity]

def oneObjFunc(chr):
	'''Receive a single chromesome and return his objetive function value'''
	
	s = 0

	for x in range(len(chr)):
		if x == len(chr) - 1:
			s += getDistance(chr[x],chr[0])
		else:
			s += getDistance(chr[x],chr[x + 1])
	return 0 - s

def objetiveFunc(population):
	'''Receive a population and return a list with the objetive 
	function values'''

	ofValues = []

	for chr in population:
		ofValues.append(oneObjFunc(chr))
	return ofValues

def chrToString(chr):
	'''Receive a chromesome (a list of int) and return a string representation'''

	st = []
	aux = 0

	for gen in chr:
		aux += 1
		st.append(str(aux) + '. ' + cities[gen])

	return str(st).strip('[]')

def fitness(population):
	'''Receive a population and return a list of floats with the fitness 
	function values. To do that the objetiveFunc() function is needed '''

	ofValues = objetiveFunc(population)
	ffValues = []
	sumOF = sum(ofValues)
	for x in ofValues:
		ffValues.append(float('%.9f'%(x / sumOF)))
	return ffValues

def newRoulette(population):
	'''Receive a population and return a roulette, a list where the index of 
	each chromesome appears proportionaly to its fitness function values'''
	
	roulette = []
	ffValues = fitness(population)
	for chrIndex in range(len(ffValues)):
		aux = int(ceil(ffValues[chrIndex] * 100)) if int(ceil(ffValues[chrIndex] * 
					100)) != 0 else 1
		for x in range(aux):
			roulette.append(chrIndex)
	for x in range(len(roulette) - 100):
		roulette.pop(randrange(len(roulette) - 1))
	return roulette

def selector(population):
	'''Return a list with the indexes of the chromosome that will be parents of
	the next generation'''

	roulette = newRoulette(population)
	parents = []
	for x in range(len(population)):
		parents.append(roulette[randrange(len(roulette) - 1)])
	return parents

def crossover(population, coChance):
	'''Receive a population and the chance of cross-over and return a population
	with the (unmutated) chromosome for the next generation'''

	def helper(dad, mom):
#		^ only for not repeat code
#		Inicialize a new son
		son = []
		for x in range(chrLen): son.append(-1)

		cursor = 0
		for x in range(chrLen):
			son[cursor] = dad[cursor]
			if mom[cursor] in son:
				break
			elif mom[cursor] not in dad:
				break
			else: 
				cursor = dad.index(mom[cursor])
		for x in range(len(son)):
			if son[x] == -1 : son[x] = mom[x] 
		return son

	parents = selector(population)
	chrLen = len(population[0])
	nextPopulation = []

	for x in filter(lambda n : n % 2 != 0, range(len(population))):
		nextPopulation.append(helper(population[parents[x]], population[parents[x - 1]]))
		nextPopulation.append(helper(population[parents[x - 1]], population[parents[x]]))

	return nextPopulation

def mutation(population, mChance):
	'''Receive a cross-overed population and return the next iteration 
	population doing a random mutation on a gen per chromosome, un function
	of the mutation chance (mChance)'''

	chrLen = len(population[0])
	nextPopulation = []
	for x in population:
		if (random() <= mChance):
			i = randrange(chrLen)
			while True:
				n = randrange(23)
				if n != x[i] : 
					x[i] = n
					break
		nextPopulation.append(x)
	return nextPopulation

def fight(chr1, chr2):
	'''Receive 2 chromosomes and return the bes in terms their decimal values'''
	if oneObjFunc(chr1) > oneObjFunc(chr2):
		return chr1
	else:
		return chr2

def championship(population):
	'''Receive a population and return the best chromesome in terms of their
	decimal values'''
	champion = population[0]
	for x in range(1, len(population) - 1):
		champion = fight(champion, population[x])
	return champion

#	-------------^^^ re-wrote functions for this excercise ^^^-------------
#	-------------vvv    functions for the heuristic part   vvv-------------

def allYourBaseAreBelongToUs(city, road = []):
	'''404: DocString not found! write one now!'''

	def nearest(road):
		m = 10000
		for x in distances[road[-1]]:
			if x == 0:
				continue
			elif distances[road[-1]].index(x) in road:
				continue
			elif x < m:
				m, x = x, m
		return distances[road[-1]].index(m)

	if len(road) == len(cities): 
		print('[!]: Road is Full.')
		return road
	elif len(road) == 0:
		road.append(city)
	while len(road) != len(cities):
		road.append(nearest(road))
	return road



def roadMaker(city, road = []):
	'''Like a shoemaker, but with roads'''
	
