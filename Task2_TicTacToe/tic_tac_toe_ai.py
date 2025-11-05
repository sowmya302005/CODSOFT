# -----------------------------------------
# CODSOFT - Task 2 : Tic Tac Toe AI
# Created by: Shetty Sowmya
# -----------------------------------------

import math

# Display the board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()

# Check if someone won
def check_winner(board):
    # Rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI chooses best move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter col (0, 1, 2): "))

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move(board)
        print("AI has played:")
        print_board(board)

        if check_winner(board) == "O":
            print("😎 AI wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a tie!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
