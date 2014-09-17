from lib import *
import data

c = 0
for city in cities:
	print('%d. ' % c + city)
	c += 1
print('23. Buscar Mejor Combinacion')

opc = int(input('Ciudad de partida: '))
while not (opc >= 0 and opc <= 23):
	print('[!]: Opcion Invalida')
	opc = int(input('Ciudad de partida: '))

if opc == 23:
	championObjFunc = -10000
	nerv = []
	for x in range(len(cities)):
		nerv.append(allYourBaseAreBelongToUs(x, []))
	champion = max(nerv, key = lambda r: oneObjFunc(r))
else:
	champion = allYourBaseAreBelongToUs(opc)

print('''
Final Result:
=============
''')
print('- Distance: %d' % abs(oneObjFunc(champion)))
print('- Route:')
c = 0
aux = []
for x in champion:
	c += 1
	aux.append('%d. ' % c + cities[x])
print(str(aux).replace('[', '').replace(']', '').replace('\'', ''))