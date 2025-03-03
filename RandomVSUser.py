import random

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

def randomMove(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (-1, -1)

def playGame():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("\nGame starts! You are (O), and the bot is (X).\n")
    print_board(board)

    while True:
        # User's turn
        while True:
            try:
                row = int(input("Enter Row (0-2): "))
                col = int(input("Enter Column (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Invalid Move, try again.")
            except ValueError:
                print("Invalid input. Enter numbers between 0 and 2.")

        print("\nYou made a move:")
        print_board(board)

        if checkWinner(board, 'O'):
            print("\nCongratulations! You (O) win!\n")
            return

        if boardFull(board):
            print("\nIt's a Tie!\n")
            return

        # Bot's turn
        row, col = randomMove(board)
        board[row][col] = 'X'
        print("\nBot (X) makes a move:")
        print_board(board)

        if checkWinner(board, 'X'):
            print("\nBot (X) wins! Better luck next time.\n")
            return

        if boardFull(board):
            print("\nIt's a Tie!\n")
            return

playGame()
