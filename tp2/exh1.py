from item import Item
from bag import Bag

def makeBag(pattern, dic):
	aux = []
	for x in range(0 , len(pattern)):
		if pattern[x] == 1:
			aux.append(dic[x])
	return Bag(aux)
	


Items = [Item(150,20), Item(325,40), Item(600,50), Item(805,36), Item(430,25), Item(1200,64), Item(770,54), Item(60,18), Item(930,46), Item(353,28)]

bb = Bag()

for a in range(0, 2):
	for b in range(0, 2):
		for c in range(0, 2):
			for d in range(0, 2):
				for e in range(0, 2):
					for f in range(0, 2):
						for g in range(0, 2):
							for h in range(0, 2):
								for i in range(0, 2):
									for j in range(0, 2):
										pattern = [a,b,c,d,e,f,g,h,i,j]
										bag = makeBag(pattern, Items)
										if bag.getSize() <= 4200:
											if bag.getTotalValue() >= bb.getTotalValue():
												bb = bag
print(bb)




