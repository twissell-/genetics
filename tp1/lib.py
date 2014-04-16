import random

def randMatrix(height, width, range):
	'''This function returns a matrix of height x width filled up with random 
	numbers from 0 to range - 1'''
	
	gens = []

	for x in xrange(0,height):
		gens.append([])
		for y in xrange(0,width):
			gens[x].append(random.randrange(range))
	return gens

def binToDec(matrix):
	'''Receive a list of lists of 0 and 1 and return a single list with the 
	decimal value of he binary list'''

	dec = []

	for x in matrix:
		aux = str(x).strip('[]')
		dec.append(int(aux.replace(', ', ''), 2))
	return dec

def objetiveFunc(decPopulation, coef):
	'''Receive a list with the decimal values of each chromesome in a population
	and de coef param and return a list with the objetive function values'''

	ofValues = []
	for x in decPopulation:
		ofValues.append((x / coef) ** 2)
	return ofValues

def fitness(ofValues):
	'''Receive a list with the objetive function values and return a list with
	the fitness function values '''

	ffValues = []
	sumOF = sum(ofValues)
	for x in ofValues:
		ffValues.append('%.3f'%(x / sumOF))
	return ffValues



