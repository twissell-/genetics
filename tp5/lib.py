from operator import attrgetter
#Datos

rewards = {('A', 'A') : [1,1], ('A', 'N') : [5,0], ('N', 'A') : [0,5], ('N', 'N') : [4,4]}

def game(player1, player2):
	play = (player1.play() , player2.play())
	player1.points += rewards[play][0]
	player2.points += rewards[play][1]
	player1.lastGame = player2.lastGame = play

def match(player1, player2):
	player1.reset()
	player2.reset()
	for x in range(10):
		game(player1, player2)

def championship(players, fixture):
	f = True
	for game in fixture:
		match(players[game[0]], players[game[1]])
		if f:
			best = [players[game[0]], players[game[1]]]
			f = False
		else:
			if best[0].points < players[game[0]].points and best[1].points < players[game[1]].points:
				best = [players[game[0]], players[game[1]]]
	return best