import numpy as np


class RandomPlayer:
	def __init__(self, seed=None):
		self.playernum = 0
		if seed is not None:
			self.random = np.random.RandomState(seed)
		else:
			self.random = np.random.RandomState()
	
	def pickmove(self, game):
		moves = game.validmoves()
		move = moves[self.random.randint(len(moves))]
		return move
