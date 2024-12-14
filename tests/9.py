# Creating a simple Q-learning agent to navigate a maze environment

# The maze will be represented as a 2D grid where:

# - 0 represents empty paths

# - 1 represents walls

# - 2 represents the goal

# - 3 represents the agent's current position

# Steps:

# 1. Create the maze environment

# 2. Implement Q-learning algorithm

# 3. Train the agent

# 4. Visualize the results



import numpy as np



import matplotlib.pyplot as plt



class MazeEnvironment:

    def __init__(self):

        # Initialize maze (0=path, 1=wall, 2=goal)

        self.maze = np.array([

            [0, 0, 0, 1],
                            
            [1, 1, 0, 1],

            [0, 0, 0, 0],

            [1, 1, 1, 2]

        ])

        self.start_position = (0, 0)

        
        self.goal_position = (3, 3)

        

    def reset(self):

        
        return self.current_position

    

    def get_possible_actions(self):

        actions = []

        x, y = self.current_position

        

        # Check all possible moves (up, right, down, left)

        possible_moves = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]

        

        for move in possible_moves:

            if (0 <= move[0] < self.maze.shape[0] and 
                
                0 <= move[1] < self.maze.shape[1] and 

                self.maze[move] != 1):

                actions.append(move)

        

        
    

    def step(self, action):

        if action not in self.get_possible_actions():

            
        

        
        

        # Check if goal is reached

        if self.current_position == self.goal_position:

            
        

        


class QLearningAgent:

    def __init__(self, maze_size):

        self.q_table = {}

        self.learning_rate = 0.1

        self.discount_factor = 0.95

        self.epsilon = 0.1

        
    

    def get_action(self, state, possible_actions):

        if random.random() < self.epsilon:

            return random.choice(possible_actions)

        

        return self.get_best_action(state, possible_actions)

    

    def get_best_action(self, state, possible_actions):

        best_value = float('-inf')

        
        

        for action in possible_actions:

            state_action = (state, action)

            if state_action not in self.q_table:

                self.q_table[state_action] = 0

            

            if self.q_table[state_action] > best_value:

                best_value = self.q_table[state_action]

                
        

        return best_action or random.choice(possible_actions)

    

    def learn(self, state, action, reward, next_state, possible_next_actions):

        state_action = (state, action)

        if state_action not in self.q_table:

            self.q_table[state_action] = 0

        

        best_next_value = float('-inf')

        for next_action in possible_next_actions:

            next_state_action = (next_state, next_action)

            if next_state_action not in self.q_table:

                self.q_table[next_state_action] = 0

            best_next_value = max(best_next_)