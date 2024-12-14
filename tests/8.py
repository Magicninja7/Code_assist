# Game Idea: Create a simplified chess-like game called "Battle Royale"

# - 6x6 board instead of 8x8

# - Only 3 types of pieces: Warriors (move 1 square any direction), Archers (move 2 squares diagonally), Kings (move 1 square any direction)

# - Each player starts with 1 King, 2 Archers, and 4 Warriors

# - Goal is to capture the enemy King

# - Turn-based movement with simple console-based visualization



# Steps:

# 1. Create the game board and initialize pieces

# 2. Display board function

# 3. Implement piece movement rules

# 4. Create turn system

# 5. Add win condition check

# 6. Main game loop



import numpy as np





class BattleRoyale:

    def __init__(self):

        self.board = np.full((6, 6), '.')

        self.current_player = 1

        
        

        # Initialize pieces (1 for player 1, 2 for player 2)

        # W = Warrior, A = Archer, K = King

        

        # Player 1 pieces (bottom)

        self.board[5, 2:4] = ['K1', 'W1']

        self.board[4, 1:5] = ['W1', 'A1', 'A1', 'W1']

        

        # Player 2 pieces (top)

        self.board[0, 2:4] = ['W2', 'K2']

        self.board[1, 1:5] = ['W2', 'A2', 'A2', 'W2']



    def display_board(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n  0 1 2 3 4 5")

        print("  -----------")

        for i in range(6):

            row = f"{i}|"

            for j in range(6):

                piece = str(self.board[i, j])

                if piece == '.':

                    row += '. '

                else:

                    row += piece + ' '

            print(row)

        print()



    def is_valid_move(self, start, end, piece):

        
        
        

        # Check if destination is empty or contains enemy piece

        if self.board[end_row, end_col] != '.':

            if self.board[end_row, end_col][1] == str(self.current_player):

                
        

        piece_type = piece[0]

        

        if piece_type == 'W':  # Warrior

            return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1

        

        elif piece_type == 'A':  # Archer

            return abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2

        

        elif piece_type == 'K':  # King

            return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1

        

        


    def make_move(self):

        while True:

            try:

                print(f"Player {self.current_player}'s turn")

                start = tuple(map(int, input("Enter start position (row col): ").split()))

                end = tuple(map(int, input("Enter end position (row col): ").split()))

                

                if not (0 <= start[0] <= 5 and 0 <= start[1] <= 5 and 
                        
                        0 <= end[0] <= 5 and 0 <= end[1] <= 5):

                    print("Position out of bounds!")

                    
                

                piece = self.board[start[0], start[1]]

                if