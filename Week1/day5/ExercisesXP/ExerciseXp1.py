
'''
mini-project - tik tac toe

What you will create
A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.



tic-tac-toe



Instructions:
Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.



Step 1: Representing the Game Board

You’ll need a way to represent the 3x3 grid.
A list of lists (a 2D list) is a good choice.
Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).


Step 2: Displaying the Game Board

Create a function called display_board() to print the current state of the game board.
The output should visually represent the 3x3 grid.
Think about how to format the output to make it easy to read.


Step 3: Getting Player Input

Create a function called player_input(player) to get the player’s move.
The function should ask the player to enter a position (e.g., row and column numbers).
Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
Think about how to ask the user for input, and how to validate that input.


Step 4: Checking for a Winner

Create a function called check_win(board, player) to check if the current player has won.
The function should check all possible winning combinations (rows, columns, diagonals).
If a player has won, return True; otherwise, return False.
Think about how to check every possible winning combination.


Step 5: Checking for a Tie

Create a function to check if the game has resulted in a tie.
The function should check if all positions of the board are full, without a winner.


Step 6: The Main Game Loop

Create a function called play() to manage the game flow.
Initialize the game board.
Use a while loop to continue the game until there’s a winner or a tie.
Inside the loop:
Display the board.
Get the current player’s input.
Update the board with the player’s move.
Check for a winner.
Check for a tie.
Switch to the next player.
After the loop ends, display the final result (winner or tie).
'''

top_bottom_line =   '*****************'
between_line =      '*  ---|---|---  *'


board = [[" "," "," "],[" "," "," "],[" "," "," "]]

player_1 = ''
player_2 = ''
who_turn = ''

def display_board():
    print('TIC TAC TOE')
    print(top_bottom_line)
    
    for i, row in enumerate(board):
        print(f'*    {row[0]}| {row[1]} | {row[2]}   *')

        if i < 2:
            print(between_line)
    
    print(top_bottom_line)

def player_input(player):
    print(f"Player {player}'s turn...")
    row = (input('Enter row: '))
    col = (input('Enter col: '))
    if row.isdigit() and col.isdigit():
        row = int(row)-1
        col = int(col)-1
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = player
            return
    print('the input isnt valid enter again')
    return player_input(player)
    
def check_win(board, player):

    # Check rows
    for row, row_list in enumerate(board):
        line = "".join(row_list)
        if line == player * 3:
            return True

    # Check columns
    colom1 = ""
    colom2 = ""
    colom3 = ""

    for row in range(3):
        colom1 += board[row][0]
        colom2 += board[row][1]
        colom3 += board[row][2]

    if player * 3 in (colom1, colom2, colom3):
        return True

    # Check diagonals
    diagnal1 = board[0][0] + board[1][1] + board[2][2]
    diagnal2 = board[0][2] + board[1][1] + board[2][0]

    if player * 3 in (diagnal1, diagnal2):
        return True

    return False
    
def check_tie(board):
    if check_win(board, 'X') or check_win(board, 'O'):
        return False
    collect = ""
    for row in board:
        collect += "".join(row)       
    if " " in collect:
        return False
    else: return True

def play():
    print('welcome to TIC TAC TOE\n')
    player = "X"
    while True:
        display_board()
        player_input(player)
        if check_win(board, player):
            display_board()
            print(f'The winner is {player}')
            
            return
        elif check_tie(board):
            display_board()
            print('It is a tie')
            
            return
        if player == "X":
            player = "O"
        else: player = "X"

play()