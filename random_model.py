from random import choice

class RandomModel:
	def __init__(self, player):
		self.player = player
	def choose_move(self,e):
		moves = e.get_moves(self.player)
		return choice(moves)