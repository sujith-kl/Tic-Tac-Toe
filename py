import math

# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Utility function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

# Function to check if the game is a tie
def is_tie(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_tie(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function for the AI to make its move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = AI

# Function for the human player to make a move
def human_move(board, row, col):
    if board[row][col] == EMPTY:
        board[row][col] = HUMAN
        return True
    return False

# Function to print the current board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Main game loop
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # Human's turn
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if human_move(board, row, col):
            print_board(board)
            if check_winner(board, HUMAN):
                print("You win!")
                break
            if is_tie(board):
                print("It's a tie!")
                break
        else:
            print("Invalid move! Try again.")

        # AI's turn
        ai_move(board)
        print("AI's move:")
        print_board(board)
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_tie(board):
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
