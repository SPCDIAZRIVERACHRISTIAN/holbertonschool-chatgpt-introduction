#!/usr/bin/python3
def print_board(board):
    """
    Function Description:
    Print the current state of the Tic-Tac-Toe board.

    Parameters:
    - board: A 3x3 list representing the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function Description:
    Check if there is a winner on the Tic-Tac-Toe board.

    Parameters:
    - board: A 3x3 list representing the Tic-Tac-Toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
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

def tic_tac_toe():
    """
    Function Description:
    Run the Tic-Tac-Toe game loop.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and any(" " in row for row in board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input! Row and column values must be between 0 and 2.")

    print_board(board)
    if check_winner(board):
        print("Player " + player + " wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
