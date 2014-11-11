from itertools import *
from player import *
from lib import *

# Genera los jugadores
players = [Player(gen) for gen in product(['A', 'N'], repeat = 6)]
# genera todos los enfrentamientos posibles.
fixture = product([x for x in range(64)], repeat = 2)

print(championship(players, fixture))