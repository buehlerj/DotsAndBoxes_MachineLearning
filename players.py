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


class AIPlayer:
	def __init__(self, rho=0.2, epsilonDecayRate = 0.99, epsilon=1.0):
		self.playernum = 0
		self.rho = rho
		self.epsilonDecayRate = epsilonDecayRate
		self.epsilon = epsilon
		self.Q = {}

	def pickmove(self, game):
		next_move = self.__epsilonGreedy(game.validmoves())
		return next_move

	def __epsilonGreedy(self, valid_moves):
		if np.random.uniform() < self.epsilon:
			move_index = np.random.randint(len(valid_moves))
			return valid_moves[move_index]
		else:
			next_move = valid_moves[0]
			next_probability = self.Q.get((tuple(next_move)), 0)

			for m in valid_moves:
				probability_m = self.Q.get((tuple(m)), 0)
				if probability_m > next_probability:
					next_move = m
					next_probability = probability_m

			return next_move
