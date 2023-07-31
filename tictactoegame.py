def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)

        player = players[turn]
        print(f"It's player {player}'s turn.")
        
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Congratulations! Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            turn = (turn + 1) % 2
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()