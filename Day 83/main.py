board = [' ' for _ in range(9)]

def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True

    if board[2] == board[4] == board[6] != ' ':
        return True

    return False

def check_tie():
    return ' ' not in board

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    player = 'X'

    while not check_win() and not check_tie():
        move = int(input(f"Player {player}, enter a number (1-9) to place your marker: ")) - 1

        if board[move] == ' ':
            board[move] = player
            player = 'O' if player == 'X' else 'X'
            print_board()
        else:
            print("That spot is taken. Choose another.")

    if check_win():
        print(f"Congratulations! Player {player} wins!")
    else:
        print("It's a tie!")

play_game()
