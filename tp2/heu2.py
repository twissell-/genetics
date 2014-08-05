from item import Item
from bag import Bag
from operator import attrgetter

items = [Item(1800,72), Item(600,36), Item(1200,60)]
b = Bag()

while True:
	nxt = items.pop(items.index(max(items, key=attrgetter('_coef'))))
	if b.getSize() + nxt.getVolume() <= 3000:
		b.add(nxt)
	else:
		break
print(b)