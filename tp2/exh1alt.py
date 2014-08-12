from item import Item
from bag import Bag

def makeBag(pattern, dic):

	pattern = list(bin(pattern))
	pattern.pop(0)
	pattern.pop(0)
	while len(pattern) < len(dic):
		pattern.insert(0, '0')
	aux = []
	for x in range(0 , len(pattern)):
		if pattern[x] == '1':
			aux.append(dic[x])
	return Bag(aux)
	

items = [Item(150,20,1), Item(325,40,2), Item(600,50,3), Item(805,36,4), Item(430,25,5), Item(1200,64,6), Item(770,54,7), Item(60,18,8), Item(930,46,9), Item(353,28,10)]

bb = Bag()

for x in range(0,1024):
	bag = makeBag(x, items)
	if bag.getSize() <= 4200:
		if bag.getTotalValue() >= bb.getTotalValue():
			bb = bag
print(bb)