import numpy as np
from MazeSolver.environment.actions import *
class Agent(object):
    def __init__(self, maze, alpha, randomFactor):
        self.stateHistory = [((0, 0), 0)]  # List of tuple with the state reward pair
        self.randomFactor = randomFactor
        # learning rate
        self.alpha = alpha
        # REWARDS
        self.G = {}  # key is the state and value is the estimate of future reward
        self.initReward(maze)

    def initReward(self, maze):
        size = maze.size
        for y in range(size):
            for x in range(size):
                self.G[(y, x)] = np.random.uniform(low=-1.0, high=-0.1)

    def learn(self):
        # This ensures that the heuristic is consistant
        target = 0  # The reward at the end of the maze is zero as we reached the final destination
        for prev, reward in reversed(self.stateHistory):
            # oldReward = oldReward + learning rate * (actual reward - old reward)
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            # Current reward is the target reward of previous actions
            # Gradual decrease of the value will occure
            # duo to the fact that we only add positive number on the end goal
            # so the futher away we are from the goal the less the cell learns this is the way
            target += reward
        # Restarting the episode (the chain of actions that lead to the current result)
        self.stateHistory = []
        # to go from exploration to exploitation strategy
        self.randomFactor -= 10e-5

    # Allowed moves: a list of actions according to the current state of the agent
    # up - down - left - right
    def chooseAction(self, state, allowedMoves):
        # Minus infinity
        maxG = -10e15
        nextMove = None
        randomN = np.random.random()
        if randomN < self.randomFactor:
            nextMove = np.random.choice(allowedMoves)
        else:
            for action in allowedMoves:
                # apply action to the current state
                newState = tuple([sum(x) for x in zip(state, actionSpace[action])])
                # future reward estimate of the new state >= the current estimate
                if self.G[newState] >= maxG:
                    nextMove = action
                    maxG = self.G[newState]
        return nextMove

    def updateStateHistory(self, state, reward):
        self.stateHistory.append((state, reward))
