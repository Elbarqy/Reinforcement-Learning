import matplotlib.pyplot as plt
from MazeSolver.agent.agent import Agent
from MazeSolver.environment.environment import Maze
if __name__ == '__main__':
    maze = Maze()
    robot = Agent(maze, alpha=0.1, randomFactor=0.25)
    moveHistory = []
    for i in range(5000):
        if i % 1000 == 0:
            print(i)
        while not maze.isGameOver():
            state, _ = maze.getStateAndReward()
            action = robot.chooseAction(state, maze.allowedStates[state])
            maze.updateToMaze(action)
            state, reward = maze.getStateAndReward()
            robot.updateStateHistory(state, reward)
            if maze.steps > 1000:
                # it doesn't really matter
                maze.robotPosition = (5, 5)
        robot.learn()
        moveHistory.append(maze.steps)
        maze = Maze()
    print("Total number of steps is to complete the journey is : " + str(moveHistory[-1]))
    plt.semilogy(moveHistory, 'g--')
    plt.legend('alpha=0.1')
    plt.xlabel("Number of steps")
    plt.savefig('result')
    plt.show()


