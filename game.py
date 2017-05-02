import numpy as np


class Game:
	def __init__(self):
		self.score = [0, 0]
		# Initialize an empty board
		self.board = np.full((11,6), False, dtype=bool)
		# Fill the invalid lines
		for r in [0, 2, 4, 6, 8, 10]:
			self.board[r, 5] = True

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
		moves = []
		for r in range(self.board.shape[0]):
			for c in range(self.board.shape[1]):
				if not self.board[r, c]:
					moves += [(r, c)]
		return moves
	
	def taketurn(self, p, printturns=False):
		turndone = False
		while not turndone:
			mv = p.pickmove(self)
			self.board[mv] = True
			# Check for a new filled in box
			newpoints = 0
			r = mv[0]
			c = mv[1]
			# Even Row
			if r % 2 == 0:
				# Check top
				if (r != 0) and (self.board[r - 1, c] and self.board[r - 2, c] and self.board[r - 1, c + 1]) == True:
					newpoints += 1
				# Check bottom
				if (r != 10) and (self.board[r + 1, c + 1] and self.board[r + 2, c] and self.board[r + 1, c]) == True:
					newpoints += 1
			# Odd Row
			else:
				# Check left
				if (c != 0) and (self.board[r + 1, c - 1] and self.board[r, c - 1] and self.board[r - 1, c - 1]) == True:
					newpoints += 1
				# Check right
				if (c != 5) and (self.board[r - 1, c] and self.board[r, c + 1] and self.board[r + 1, c + 1]) == True:
					newpoints += 1
			self.score[p.playernum] += newpoints

			if printturns:
				print("-----------------")
				print("Player:\t" + str(p.playernum))
				print("Move:\t" + str(mv))
				print("New Points:\t" + str(newpoints))
				print(self)
				print(self.score)

			if newpoints == 0 or not self.validmoves():
				turndone = True

	def play(self, p1, p2, printturns=False):
		p1.playernum = 0
		p2.playernum = 1
		while len(self.validmoves()) is not 0:
			self.taketurn(p1, printturns=printturns)
			if len(self.validmoves()) is not 0:
				self.taketurn(p2, printturns=printturns)
