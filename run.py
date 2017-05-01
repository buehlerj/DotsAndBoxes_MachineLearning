import game
import players

p1 = players.RandomPlayer(0)
p2 = players.RandomPlayer(1)
g = game.Game()
print(g.board)
g.play(p1, p2)
print(g.board)