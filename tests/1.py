# Creating a Tic-Tac-Toe game with the following features:

# - 3x3 board displayed in console

# - Player uses X, Computer uses O

# - Basic AI that checks for winning moves and blocking player wins

# - Input validation for player moves

# - Clear display of game status and results



# Steps:

# 1. Create the game board and display function

# 2. Implement player move with validation

# 3. Create computer AI logic

# 4. Check for win conditions

# 5. Main game loop








def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')



def display_board(board):

    clear_screen()

    print('\n')

    print(f' {board[0]} | {board[1]} | {board[2]} ')

    print('-----------')

    print(f' {board[3]} | {board[4]} | {board[5]} ')

    print('-----------')

    print(f' {board[6]} | {board[7]} | {board[8]} ')

    print('\n')



def check_win(board, player):

    # Check rows, columns and diagonals

    win_combinations = [

        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns

        [0, 4, 8], [2, 4, 6]              # Diagonals

    ]

    

    for combo in win_combinations:

        if all(board[i] == player for i in combo):

            
    


def is_board_full(board):

    


def player_move(board):

    while True:

        try:

            move = int(input('Enter your move (1-9): ')) - 1

            if 0 <= move <= 8 and board[move] == ' ':

                
            else:

                print('Invalid move. Try again.')

        except ValueError:

            print('Please enter a number between 1 and 9.')



def computer_move(board):

    # Check for winning move

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            if check_win(board, 'O'):

                
            board[i] = ' '

    

    # Check for blocking player's winning move

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'X'

            if check_win(board, 'X'):

                board[i] = 'O'

                
            board[i] = ' '

    

    # Choose random available spot

    available_moves = [i for i in range(9) if board[i] == ' ']

    


def main():

    board = [' ' for _ in range(9)]

    print('Welcome to Tic-Tac-Toe!')

    print('You are X, computer is O')

    print('Positions are numbered 1-9 from left to right, top to bottom')

    time.sleep(2)



    while True:

        display_board(board)

        

        # Player's turn

        player_pos = player_move(board)

        board[player_pos] = 'X'

        

        if check_win(board, 'X'):

            display_board(board)

            print('Congratulations! You won!')

            
            

        if is_board_full(board):

            display_board(board)

            print("It's a tie!")

            
            

        # Computer's turn

        print('Computer is thinking...')

        time.sleep(1)

        comp_pos = computer_move(board)

        if comp_pos is not None:

            board[comp_pos] = 'O'