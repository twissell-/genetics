import lib

COEF = 2. ** 30. - 1.

popu = lib.randMatrix(10, 30, 2)

print sum(lib.binToDec(popu))

print lib.fitness(lib.objetiveFunc(lib.binToDec(popu), COEF))

