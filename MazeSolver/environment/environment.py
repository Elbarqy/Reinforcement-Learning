import numpy as np
from MazeSolver.environment.actions import *
class Maze(object):
    def __init__(self):
        self.allowedStates = {}  # (x,y) : [actions]
        self.size = 6
        self.maze = np.zeros((6, 6))
        self.maze[5, :5] = 1
        self.maze[:4, 5] = 1
        self.maze[2, 2:] = 1
        self.maze[3, 2] = 1
        self.maze[0, 0] = 2
        self.robotPosition = (0, 0)
        self.steps = 0
        self.constructAllowedStates()

    def printMaze(self):
        print('---------------------------------')
        for row in self.maze:
            for col in row:
                if col == 0:
                    print('', end='\t')
                elif col == 1:
                    print('X', end='\t')
                elif col == 2:
                    print('R', end='\t')
            print('\n')
        print('---------------------------------')

    def isAllowedCell(self, state, action):
        y, x = state
        y += actionSpace[action][0]
        x += actionSpace[action][1]
        if y < 0 or x < 0 or y > 5 or x > 5:
            return False
        if self.maze[y, x] == 0 or self.maze[y, x] == 2:
            return True
        else:
            return False

    def constructAllowedStates(self):
        allowedStates = {}  # key:state, value: actions
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                if self.maze[y, x] != 1:
                    allowedStates[(y, x)] = []
                    for action in actionSpace:
                        if self.isAllowedCell((y, x), action):
                            allowedStates[(y, x)].append(action)
        self.allowedStates = allowedStates

    def updateToMaze(self, action):
        y, x = self.robotPosition
        self.maze[y, x] = 0
        y += actionSpace[action][0]
        x += actionSpace[action][1]
        self.robotPosition = (y, x)
        self.maze[y, x] = 2
        self.steps += 1

    def isGameOver(self):
        if self.robotPosition == (5, 5):
            return True
        else:
            return False

    def getStateAndReward(self):
        reward = self.giveReward()
        return self.robotPosition, reward

    def giveReward(self):
        if self.robotPosition == (5, 5):
            return 0
        else:
            return -1