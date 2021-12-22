import numpy as np
import matplotlib.pyplot as plt


class Bandit(object):
    def __init__(self, numArms, trueRewards, epsilon):
        self.Q = [0 for _ in range(numArms)]
        self.N = [0 for _ in range(numArms)]
        self.numArms = numArms
        self.epsilon = epsilon
        self.trueRewards = trueRewards
        self.lastAction = None

    def pull(self):
        rand = np.random.random()
        whichArm = None
        if rand <= self.epsilon:
            whichArm = np.random.choice(self.numArms)
        elif rand > self.epsilon:
            a = np.array([approx for approx in self.Q])
            # choose a random arm with the same max value
            whichArm = np.random.choice(np.where(a == a.max())[0])
        self.lastAction = whichArm
        return np.random.randn() + self.trueRewards[whichArm]

    def updateMean(self, sample):
        whichArm = self.lastAction
        self.N[whichArm] += 1
        self.Q[whichArm] = self.Q[whichArm] + 1.0 / self.N[whichArm] * (sample - self.Q[whichArm])


def simulate(numArms, epsilon, numPulls):
    rewardHistory = np.zeros(numPulls)
    for j in range(2000):
        rewards = [np.random.randn() for _ in range(numArms)]
        bandit = Bandit(numArms, rewards, epsilon)
        if j % 200 == 0:
            print(j)
        for i in range(numPulls):
            reward = bandit.pull()
            bandit.updateMean(reward)
            rewardHistory[i] += reward

    average = rewardHistory / 2000
    print("Completed the simulation process")
    return average


if __name__ == '__main__':
    numActions = 5
    run1 = simulate(numActions, epsilon=0.1, numPulls=1000)
    run2 = simulate(numActions, epsilon=0.001, numPulls=1000)
    run3 = simulate(numActions, epsilon=0.0, numPulls=1000)
    plt.plot(run1, 'b--', run2, 'r--', run3, 'g--')
    plt.legend(['epsilon=0.1', 'epsilon=0.01', 'epsilon=0.0'])
    plt.savefig('result')
    plt.show()
