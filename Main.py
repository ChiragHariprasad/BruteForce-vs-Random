import random

def checkWinner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def boardFull(board):
    return not any(board[i][j] == ' ' for i in range(3) for j in range(3))

def minimax(board, player):
    if checkWinner(board, 'X'):
        return 1
    elif checkWinner(board, 'O'):
        return -1
    elif boardFull(board):
        return 0

    bestScore = float('-inf') if player == 'X' else float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = minimax(board, 'O' if player == 'X' else 'X')
                board[i][j] = ' '  # Undo move
                bestScore = max(bestScore, score) if player == 'X' else min(bestScore, score)

    return bestScore

def findBestMove(board):
    bestMove = (-1, -1)
    bestScore = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 'O')
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

    while True:
        # Dumb AI ("O") move
        row, col = randomMove(board)
        board[row][col] = 'O'

        if checkWinner(board, 'O'):
            print(f"Game {game_number}: Dumb AI (O) wins!")
            return "O"
        if boardFull(board):
            print(f"Game {game_number}: It's a Tie!")
            return "Tie"

        # Smart AI ("X") move
        row, col = findBestMove(board)
        board[row][col] = 'X'

        if checkWinner(board, 'X'):
            print(f"Game {game_number}: Smart AI (X) wins!")
            return "X"
        if boardFull(board):
            print(f"Game {game_number}: It's a Tie!")
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

# Print final scores
print("\nFinal Scores after 50 Games:")
print(f"Smart AI (X) Wins: {X_wins}")
print(f"Dumb AI (O) Wins: {O_wins}")
print(f"Ties: {ties}")
