import game
import players

rho = 0.2
initialEpsilon = 1.0
epsilonDecay = 0.99
seed1 = None
seed2 = None

printturns = False

trainIterations = 2000
randTestIterations = 200
aiTrainIterations = 2000
aiTestIterations = 200

p1 = players.AIPlayer(rho=rho, epsilon=initialEpsilon, seed=seed1)
p2 = players.RandomPlayer(seed=None)

print("Dots & Boxes AI Demo")
print("--------------------------------------------")

aiWins = 0
for i in range(trainIterations):
    g = game.Game()
    if i % 2 is 0:
        g.play(p1, p2, printturns=printturns)
    else:
        g.play(p2, p1, printturns=printturns)
    if g.score.index(max(g.score)) is p1.playernum:
        aiWins += 1
    p1.epsilon *= epsilonDecay
print("Train vs. Random:\t{} wins out of {}".format(aiWins, trainIterations))

aiWins = 0
p1.train = False
for i in range(randTestIterations):
    g = game.Game()
    if i % 2 is 0:
        g.play(p1, p2, printturns=printturns)
    else:
        g.play(p2, p1, printturns=printturns)
    if g.score.index(max(g.score)) is p1.playernum:
        aiWins += 1
print("Test vs. Random:\t{} wins out of {}".format(aiWins, randTestIterations))

print("--------------------------------------------")

wins = [0, 0]
p1.train = True
p1.epsilon = initialEpsilon
p2 = players.AIPlayer(rho=rho, epsilon=initialEpsilon, seed=seed2)
p2.Q = p1.Q
for i in range(aiTrainIterations):
    g = game.Game()
    g.play(p1, p2, printturns=False)
    wins[g.score.index(max(g.score))] += 1
    p1.epsilon *= epsilonDecay
    p2.epsilon *= epsilonDecay
print("Train vs. Self:\t{} wins to {} wins".format(wins[0], wins[1]))

wins = [0, 0]
p1.train = False
p2.train = False
for i in range(aiTestIterations):
    g = game.Game()
    g.play(p1, p2, printturns=False)
    wins[g.score.index(max(g.score))] += 1
print("Test vs. Self:\t{} wins to {} wins".format(wins[0], wins[1]))

# Print the Q Dictionary
# import math
# print("Significant Q Values:\n{")
# for i in p1.Q:
#     if not math.isclose(0.0, p1.Q[i]):
#         print("\t{}: {}".format(i, p1.Q[i]))
# print("}")
