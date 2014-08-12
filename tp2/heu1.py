from item import Item
from bag import Bag
from operator import attrgetter

items = [Item(150,20,1), Item(325,40,2), Item(600,50,3), Item(805,36,4), Item(430,25,5), Item(1200,64,6), Item(770,54,7), Item(60,18,8), Item(930,46,9), Item(353,28,10)]

b = Bag()
while True:
	nxt = items.pop(items.index(max(items, key=attrgetter('_coef'))))
	if b.getSize() + nxt.getVolume() <= 4200:
		b.add(nxt)
	else:
		break
print(b)


