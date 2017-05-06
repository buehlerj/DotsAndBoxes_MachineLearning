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
		moves = game.validmoves()
		nextMove = self.__epsilonGreedy(game)
		return nextMove

	def __epsilonGreedy(self, game):
		validMoves = game.validmoves()
		if np.random.uniform() < self.epsilon:
			return np.random.choice(validMoves)
		else:
			Qs = np.array([self.Q.get((tuple(validMoves), m), 0) for m in validMoves])
			return validMoves[np.argmax(Qs)]
