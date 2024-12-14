# Creating a simple Q-learning agent to navigate a maze environment

# Steps:

# 1. Create a simple maze environment using a 2D array

# 2. Implement the Q-learning algorithm

# 3. Define state and action spaces

# 4. Create training loop

# 5. Visualize the results

# Note: This is a basic implementation with a small maze for demonstration



import numpy as np


import matplotlib.pyplot as plt




class MazeEnvironment:

    def __init__(self):

        # 0 = path, 1 = wall, 2 = goal

        self.maze = np.array([

            [0, 0, 0, 1],
                            
            [1, 1, 0, 1],

            [0, 0, 0, 0],

            [1, 1, 1, 2]

        ])

        self.start_pos = (0, 0)

        
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up



    def reset(self):

        
        return self.current_pos



    def step(self, action):

        new_pos = (self.current_pos[0] + self.actions[action][0],
                   
                  self.current_pos[1] + self.actions[action][1])

        

        # Check if new position is valid

        if (0 <= new_pos[0] < self.maze.shape[0] and 
            
            0 <= new_pos[1] < self.maze.shape[1] and 

            self.maze[new_pos] != 1):

            

            
            

            # Check if goal reached

            if self.maze[self.current_pos] == 2:

                
            

            
        

        


class QLearningAgent:

    def __init__(self, state_size, action_size):

        self.q_table = {}

        
        
        self.learning_rate = 0.1

        self.discount_factor = 0.95

        self.epsilon = 0.1



    def get_action(self, state):

        if random.random() < self.epsilon:

            return random.randint(0, self.action_size - 1)

        

        return self.get_best_action(state)



    def get_best_action(self, state):

        if state not in self.q_table:

            self.q_table[state] = np.zeros(self.action_size)

        return np.argmax(self.q_table[state])



    def update(self, state, action, reward, next_state):

        if state not in self.q_table:

            self.q_table[state] = np.zeros(self.action_size)

        if next_state not in self.q_table:

            self.q_table[next_state] = np.zeros(self.action_size)



        # Q-learning update formula

        current_q = self.q_table[state][action]

        next_max_q = np.max(self.q_table[next_state])

        new_q = current_q + self.learning_rate * (reward + self.discount_factor * next_max_q - current_q)

        


# Training loop

env = MazeEnvironment()

agent = QLearningAgent(state_size=env.maze.shape, action_size=4)

episodes = 1000

rewards_history = []



for episode in range(episodes):

    state = env.reset()

    total_reward = 0

    
    

    while not done:

        action = agent.get_action()