import numpy as np


class Game:
	class Board:
		def __init__(self):
			# Configure validmoves caching
			self.validmoves = None
			self.haschanged = True
			# Initialize an empty board
			self.array = np.full((11, 6), False, dtype=bool)
			self.shape = (11, 6)
			# Fill the invalid lines
			for r in [0, 2, 4, 6, 8, 10]:
				self.array[r, 5] = True

		def __getitem__(self, item):
			return self.array[item]

		def __setitem__(self, key, value):
			self.array[key] = value
			self.haschanged = True

		def __delitem__(self, key):
			del self.array[key]
			self.haschanged = True

		def __str__(self):
			return str(self.array)

		def getvalidmoves(self):
			if self.haschanged or not self.validmoves:
				self.validmoves = []
				for r in range(self.array.shape[0]):
					for c in range(self.array.shape[1]):
						if not self.array[r, c]:
							self.validmoves += [(r, c)]
			self.haschanged = False
			return self.validmoves

	def __init__(self):
		self.score = [0, 0]
		self.board = Game.Board()

	def __str__(self):
		space = "\u2008\u2008"
		bigspace = "  "
		dot = "\u2022"
		hline = "\u2006\u2500\u2500\u2006"
		vline = "|"
		board = ""
		for r in range(self.board.shape[0]):
			if r % 2 == 0:
				board += dot
				for c in range(self.board.shape[1] - 1):
					if self.board[r, c]:
						board += hline
					else:
						board += bigspace
					board += dot
			else:
				for c in range(self.board.shape[1]):
					if self.board[r, c]:
						board += vline
					else:
						board += space
					board += bigspace
			board += "\n"
		return board

	def validmoves(self):
		return self.board.getvalidmoves()

	def taketurn(self, player, printturns=False):
		turndone = False
		while not turndone:
			mv = player.pickmove(self)
			self.board[mv] = True
			# Check for a new filled in box
			newpoints = 0
			r = mv[0]
			c = mv[1]
			# Even Row
			if r % 2 == 0:
				# Check top
				if (r != 0) and (self.board[r - 1, c] and self.board[r - 2, c] and self.board[r - 1, c + 1]):
					newpoints += 1
				# Check bottom
				if (r != 10) and (self.board[r + 1, c + 1] and self.board[r + 2, c] and self.board[r + 1, c]):
					newpoints += 1
			# Odd Row
			else:
				# Check left
				if (c != 0) and (self.board[r + 1, c - 1] and self.board[r, c - 1] and self.board[r - 1, c - 1]):
					newpoints += 1
				# Check right
				if (c != 5) and (self.board[r - 1, c] and self.board[r, c + 1] and self.board[r + 1, c]):
					newpoints += 1
			self.score[player.playernum] += newpoints

			if printturns:
				print("-----------------")
				print("Player:\t" + str(player.playernum))
				print("Move:\t" + str(mv))
				print("New Points:\t" + str(newpoints))
				print(self)
				print(self.score)

			if newpoints == 0 or not self.validmoves():
				turndone = True

	def play(self, p1, p2, printturns=False):
		p1.pregame(0)
		p2.pregame(1)
		while len(self.validmoves()) is not 0:
			self.taketurn(p1, printturns=printturns)
			if len(self.validmoves()) is not 0:
				self.taketurn(p2, printturns=printturns)
		p1.postgame(self)
		p2.postgame(self)
