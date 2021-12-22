# What is an agent ?
anything that the agent doesn't control is part of the enviroment
the agent is only responsible for maximizing his reward
The agent has
1.   Memory of rewards
2.   Memory of the state 
3.   Random actions 
4.   Maximizes rewards

Agents generally lerns from observations

# The learning algorithm
- init G randomly
- Repeat for number of episodes
  - while game is not over
    - Get state and reward from enviroment
    - Select action
    - update enviroment
    - Get updated state and reward
    - Store new state and reward in memory
  - Replay memory of previous Episodes

  Gstate = Gstate + alpha (target - Gstate)

# Notes Regarding implementation
  `Gstate = Gstate + alpha (target - Gstate)`

We initialize Gstate to be all between -0.1 : -1 which we can interpret as follow

## things to note about the behavior of the learning process  

- All cells are bad [Unexplored]
- when reaching the goal considering alpha = 1 , target = 0 Gstate = Gstate - Gstate
- The new state would be 0 which is > -0.1
- The further you go away from the goal the less the impact of the learning factor (as all we only reward with 1 when reaching the final stage)
- it's safe to artificially place the robot on the (5,5) cell when exceeding 1000 steps as the agent would have been trapped in a loop learning would only decrease the reward in that loop

## What to note about the whole algorithm
- The agent learns only the features of the enviroments and how to deal with it
- A* is more generalized and faster compared to the training process of this algorithm
