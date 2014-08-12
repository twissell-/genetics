from item import Item
from bag import Bag

def makeBag(pattern, dic):
	aux = []
	for x in range(0 , len(pattern)):
		if pattern[x] == 1:
			aux.append(dic[x])
	return Bag(aux)
	


items = [Item(150,20,1), Item(325,40,2), Item(600,50,3), Item(805,36,4), Item(430,25,5), Item(1200,64,6), Item(770,54,7), Item(60,18,8), Item(930,46,9), Item(353,28,10)]

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
										bag = makeBag(pattern, items)
										if bag.getSize() <= 4200:
											if bag.getTotalValue() >= bb.getTotalValue():
												bb = bag
print(bb)




