import numpy as np


class RandomPlayer:
	def __init__(self, seed=None):
		self.playernum = 0
		self.seed = seed
		self.__buildRandom()

	def __buildRandom(self):
		if self.seed is not None:
			self.random = np.random.RandomState(seed=self.seed)
		else:
			self.random = np.random.RandomState()

	def pregame(self, playernum):
		self.playernum = playernum
	
	def pickmove(self, game):
		moves = game.validmoves()
		move = moves[self.random.randint(len(moves))]
		return move

	def postgame(self, game):
		return


class AIPlayer:
	def __init__(self, rho=0.2, epsilon=1.0, train=True, seed=None):
		self.playernum = 0
		self.rho = rho
		self.epsilon = epsilon
		self.Q = {}
		self.currentMove = None
		self.previousMove = None
		self.train = train
		self.seed = seed
		self.random = None
		self.__buildRandom()

	def __buildRandom(self):
		if self.seed is not None:
			self.random = np.random.RandomState(seed=self.seed)
		else:
			self.random = np.random.RandomState()

	def resetq(self):
		self.Q = {}

	def pregame(self, playernum):
		self.playernum = playernum
		self.previousMove = None
		self.currentMove = None

	def pickmove(self, game):
		self.__propagate()
		self.previousMove = self.currentMove
		moveindex = self.__epsilonGreedy(game.validmoves())
		self.currentMove = (tuple(game.validmoves()), moveindex)
		return game.validmoves()[moveindex]

	def __epsilonGreedy(self, valid_moves):
		move_index = 0
		if self.random.uniform() < self.epsilon:
			move_index = self.random.randint(len(valid_moves))
		else:
			best_probability = -1 * np.inf
			for i in range(len(valid_moves)):
				probability_m = self.Q.get((tuple(valid_moves), i), 0)
				if probability_m > best_probability:
					move_index = i
					best_probability = probability_m
		return move_index

	def __propagate(self):
		if self.train is True and self.previousMove is not None:
			temporaldifferenceerror = self.rho * (self.Q.get(self.currentMove, 0) - self.Q.get(self.previousMove, 0))
			self.Q[self.previousMove] = self.Q.get(self.previousMove, 0) + temporaldifferenceerror

	def postgame(self, game):
		if self.train is True:
			if game.score.index(max(game.score)) is self.playernum:
				# Winning move, positive reinforcement
				self.Q[self.currentMove] = 1
			else:
				# Losing move, negative reinforcement
				r = self.rho * (-1 - self.Q.get(self.currentMove, 0))
				self.Q[self.currentMove] = self.Q.get(self.currentMove, 0) + r
			self.__propagate()
