from data import distances, cities
from time import strftime
from itertools import *
from lib import *

# CONSTANTES

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

print('[i]: Running...\n')
startTime = strftime("%H:%M:%S")
varSet = []
for x in range(1,10):
	varSet.append(x)
a = 0
for road in permutations(varSet, 9):
	if a % 100 == 0:
		aux = int((a * 100) / 362880)
		print(CURSOR_UP_ONE + ERASE_LINE + '[' + '#' * int(aux/2) + 
			' ' * (50 - int(aux/2)) + '] : ' + ('%d%%') % aux)	
	r = [0] + list(road)
	if a == 0:
		br = r
	a += 1
	if getTotalDistance(r) > getTotalDistance(br):
		br = r

finalTime = strftime("%H:%M:%S")
print('[i]: Done...')

print('''
Final Result:
=============
''')
print('- Started at: %s' % startTime)
print('- Finished at: %s' % finalTime)
print('- Iterations: %d' % a)
print('- Distance: %d' % abs(getTotalDistance(br)))
print('- Route:')
c = 0
for x in br:
	c += 1
	print('%d. ' % c + cities[x])

