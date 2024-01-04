def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if (all(board[i][i] == player for i in range(3))
        or all(board[i][2 - i] == player for i in range(3))):
        return True
    return False

def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for _ in range(9):
        row, col = map(int, input(f"Player {players[current_player]}, "
                                  f"enter row and column (0-2) separated by space: ").split())

        while board[row][col] != "-":
            print("Invalid move. Try again.")
            row, col = map(int, input(f"Player {players[current_player]}, "
                                      f"enter row and column (0-2) separated by space: ").split())

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            return

        current_player = (current_player + 1) % 2

    print("It's a tie!")

tic_tac_toe()

