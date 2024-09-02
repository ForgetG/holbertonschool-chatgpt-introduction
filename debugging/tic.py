#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board with rows and columns separated by lines.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks whether there is a winner in the current board state.
    
    Returns:
    - True if there is a winner.
    - False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks whether the board is full and there is no winner, indicating a draw.
    
    Returns:
    - True if the game is a draw.
    - False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """
    Prompts the user for input and ensures it's a valid integer within the allowed range.
    
    Returns:
    - A valid integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    Handles the game loop, player turns, and determines the outcome.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")
        
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
