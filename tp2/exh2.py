from item import Item
from bag import Bag

def makeBag(pattern, dic):
	aux = []
	for x in range(0 , len(pattern)):
		if pattern[x] == 1:
			aux.append(dic[x])
	return Bag(aux)

items = [Item(1800,72,1), Item(600,36,2), Item(1200,60,3)]
bb = Bag()

for a in range(0, 2):
	for b in range(0, 2):
		for c in range(0, 2):
			pattern = [a, b, c]
			bag = makeBag(pattern, items)
			if bag.getSize() <= 3000:
				if bag.getTotalValue() >= bb.getTotalValue():
					bb = bag
print(bb)

