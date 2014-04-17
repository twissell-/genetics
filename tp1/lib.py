from random import randrange

def newPopulation(popSize, gens, range):
	'''This function returns a matrix of popSize x gens filled up with random 
	numbers from 0 to range - 1'''
	
	population = []

	for x in xrange(0, popSize):
		population.append([])
		for y in xrange(0, gens):
			population[x].append(randrange(range))
	return population

def chrToString(chr):
	'''Receive a chromesome (a list of int) and return a string representation'''

	return str(chr).strip('[]').replace(', ', '')

def binToDec(population):
	'''Receive a list of lists of 0 and 1 and return a single list with the 
	decimal value of he binary list'''

	dec = []

	for x in population:
		aux = chrToString(x)
		dec.append(int(aux, 2))
	return dec

def objetiveFunc(population, coef):
	'''Receive a population the coef param and return a list with the objetive 
	function values'''

	decPopulation = binToDec(population)
	ofValues = []
	for x in decPopulation:
		ofValues.append(float('%.2f'%((x / coef) ** 2)))
	return ofValues

def fitness(population, coef):
	'''Receive a population and return a list of floats with the fitness 
	function values. To do that the objetiveFunc() function is needed '''

	ofValues = objetiveFunc(population, coef)
	ffValues = []
	sumOF = sum(ofValues)
	for x in ofValues:
		ffValues.append(float('%.2f'%(x / sumOF)))
	return ffValues

def newRoulette(population, coef):
	'''Receive a population and return a roulette, a list where the index of 
	each chromesome appears proportionaly to its fitness function values'''
	
	roulette = []
	ffValues = fitness(population, coef)
	for chrIndex in xrange(0, len(ffValues)):
		for x in xrange(0, int(ffValues[chrIndex] * 100)):
			roulette.append(chrIndex)
	return roulette

def selector(population, coef):
	'''Return a list with the indexes of the chromesomes that will parents of
	the next generation'''

	roulette = newRoulette(population, coef)
	parents = []
	for x in xrange(0, len(population)):
		parents.append(roulette[randrange(len(roulette) - 1)])
	return parents

