import game
import players
import math

p1 = players.AIPlayer(epsilon=1.0, seed=0)
p2 = players.RandomPlayer(seed=1)
g = game.Game()
print("Test Run")
g.play(p1, p2, printturns=False)
print("-----------------")
print("Final Score:\t" + str(g.score))
print("Total Points:\t" + str(sum(g.score)))
print("-----------------")
print("Significant Q Values:\n{")
for i in p1.Q:
    if not math.isclose(0.0, p1.Q[i]):
        print("\t{}: {}".format(i, p1.Q[i]))
print("}")
