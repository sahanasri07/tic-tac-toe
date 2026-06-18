def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True

    return False


def board_full(board):
    return all(cell in ["X", "O"] for cell in board)


board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

current_player = "X"

while True:
    print_board(board)

    move = input(f"Player {current_player}, choose a position (1-9): ")

    if not move.isdigit():
        print("Please enter a valid number.")
        continue

    move = int(move)

    if move < 1 or move > 9:
        print("Choose a number between 1 and 9.")
        continue

    if board[move - 1] in ["X", "O"]:
        print("Position already taken.")
        continue

    board[move - 1] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break

    if board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"