import random
import time

def print_board(board):
    for row in board:
        print("|".join(row))
    print("---------")

def checkWinner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def boardFull(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def dfs(board, player):
    if checkWinner(board, 'X'):
        return 1
    elif checkWinner(board, 'O'):
        return -1
    elif boardFull(board):
        return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                scores.append(dfs(board, 'O' if player == 'X' else 'X'))
                board[i][j] = ' '  # Undo move

    return max(scores) if player == 'X' else min(scores)

def findBestMove(board):
    bestScore = float('-inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = dfs(board, 'O')
                board[i][j] = ' '  # Undo move
                if score > bestScore:
                    bestScore = score
                    bestMove = (i, j)
    return bestMove

def randomMove(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (-1, -1)

def playGame(game_number):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print(f"\nGame {game_number} starts!\n")
    print_board(board)

    while True:
        time.sleep(0.5)  # Small delay for better visibility

        # Dumb AI ("O") move
        row, col = randomMove(board)
        board[row][col] = 'O'
        print("\nDumb AI (O) makes a move:")
        print_board(board)

        if checkWinner(board, 'O'):
            print("\nDumb AI (O) wins!\n")
            return "O"

        if boardFull(board):
            print("\nIt's a Tie!\n")
            return "Tie"

        time.sleep(0.5)  # Delay for better visibility

        # Smart AI ("X") move
        row, col = findBestMove(board)
        board[row][col] = 'X'
        print("\nSmart AI (X) makes a move:")
        print_board(board)

        if checkWinner(board, 'X'):
            print("\nSmart AI (X) wins!\n")
            return "X"

        if boardFull(board):
            print("\nIt's a Tie!\n")
            return "Tie"

# Run 50 Games
X_wins, O_wins, ties = 0, 0, 0

for game in range(1, 51):
    result = playGame(game)
    if result == "X":
        X_wins += 1
    elif result == "O":
        O_wins += 1
    else:
        ties += 1

    time.sleep(1)  # Pause before the next game starts

# Print final scores
print("\nFinal Scores after 50 Games:")
print(f"Smart AI (X) Wins: {X_wins}")
print(f"Dumb AI (O) Wins: {O_wins}")
print(f"Ties: {ties}")
