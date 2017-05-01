import numpy as np
import players

class Game:
	def __init__(self):
		self.score = [0, 0]
		# Initialize an empty board
		self.board = np.full((11,6), False, dtype=bool)
		# Fill the invalid lines
		for r in [0, 2, 4, 6, 8, 10]:
			self.board[r, 5] = True
	
	def validmoves(self):
		moves = []
		for r in range(self.board.shape[0]):
			for c in range(self.board.shape[1]):
				if (not self.board[r, c]):
					moves += [(r, c)]
		return moves
	
	def taketurn(self, p):
		turndone = False
		while not turndone:
			mv = p.pickmove(self)
			self.board[mv] = True
			# Check for a new filled in box
			newpoints = 0
			r = mv[0]
			c = mv[1]
      # Even Row
			if mv[0] % 2 == 0:
				# Check top
				if ((self.board[r, c - 1] and self.board[r, c - 2] and self.board[r + 1, c - 1]) == True):
					newpoints += 1
				# Check bottom
				if ((self.board[r + 1, c + 1] and self.board[r, c + 2] and self.board[r, c + 1]) == True):
					newpoints += 1
			# Odd Row
			else:
				# Check left
				if ((self.board[r - 1, c + 1] and self.board[r - 1, c] and self.board[r - 1, c - 1]) == True):
					newpoints += 1
				# Check right
				if ((self.board[r, c - 1] and self.board[r + 1, c] and self.board[r, c + 1]) == True):
					newpoints += 1
			self.score[p.playernum] += newpoints
			if newpoints == 0 or not self.validmoves():
				turndone = True

	def play(self, p1, p2):
		p1.playernum = 0
		p2.playernum = 1
		while len(self.validmoves()) != 0:
			self.taketurn(p1)
			self.taketurn(p2)
