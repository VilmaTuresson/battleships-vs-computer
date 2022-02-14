from random import randint


PLAYER_BOARD = [[' '] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[' '] * 8 for i in range(8)]
COMPUTER_BOARD = [[' '] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[' '] * 8 for i in range(8)]


def print_board(board):
    """
    Function to loop out a grid.
    """
    print('  1 2 3 4 5 6 7 8')
    row_num = 1
    for row in board:
        print('%d|%s|' % (row_num, '|'.join(row)))
        row_num += 1


def get_user_input(input_type):
    """
    Functions to get user input for setting and guessing locations.
    """
    input_invalid = True
    user_input = ''
    while input_invalid:
        try:
            user_input = int(input(f'Select a {input_type} between 1 -8: \n'))
            if user_input in ['1, 2, 3, 4, 5, 6, 7, 8']:
                user_input = user_input - 1
                input_invalid = False
                return user_input
            else:
                print(f"'{user_input}' is not a valid number, please try again")
        except ValueError:
            print(f"'{user_input}' is not a valid number, please try again")


def set_user_ships(board):
    """
    Function calling the get_user_input function to place out user ships.
    """
    print('Enter coordinates to set out 4 battleships!')
    for ship in range(4):
        user_row, user_column = get_user_input()
        while board[user_row][user_column] == '@':
            print('You have already placed a ship on these coordinates')
            user_row, user_column = get_user_input()
        board[user_row][user_column] = '@'


def create_computer_ships(board):
    """
    Function to get two random intergers to place out a ship and
    trying again if there is a ship places there already.
    """
    for ship in range(4):
        computer_row = randint(0, 7)
        computer_column = randint(0, 7)
        while board[computer_row][computer_column] == '@':
            computer_row = randint(0, 7)
            computer_column = randint(0, 7)
        board[computer_row][computer_column] = '@'


def count_sunken_ships(board):
    """
    Function to increment the sunken_ships variable when
    computer or user hits a ship.
    """
    sunken_ships = 0
    for row in board:
        for column in row:
            if column == '*':
                sunken_ships += 1
    return sunken_ships


create_computer_ships(COMPUTER_BOARD)
set_user_ships(PLAYER_BOARD)

while True:
    while True:
        print_board(PLAYER_GUESS_BOARD)
        row, column = get_user_input()
        if PLAYER_GUESS_BOARD[row][column] == '*':
            print('You have already guessed that coordinate!')
        elif PLAYER_GUESS_BOARD[row][column] == '-':
            print('You have already guessed that coordinate!')
        elif COMPUTER_BOARD[row][column] == '@':
            print('You sunk a ship!')
            PLAYER_GUESS_BOARD[row][column] = '*'
            break
        else:
            print('You missed!')
            PLAYER_GUESS_BOARD[row][column] = '-'
            break
    if count_sunken_ships(PLAYER_GUESS_BOARD) == 4:
        print('You sank all your opponents ships!')
        break

    while True:
        row, column = randint(0, 7), randint(0, 7)
        if COMPUTER_GUESS_BOARD[row][column] == '*':
            row, column = randint(0, 7), randint(0, 7)
        elif COMPUTER_GUESS_BOARD[row][column] == '-':
            row, column = randint(0, 7), randint(0, 7)
        elif PLAYER_BOARD[row][column] == '@':
            COMPUTER_GUESS_BOARD[row][column] = '*'
            print('Your opponent sank one of you ships!')
            print_board(COMPUTER_GUESS_BOARD)
            break
        else:
            COMPUTER_GUESS_BOARD[row][column] = '-'
            break
    if count_sunken_ships(COMPUTER_GUESS_BOARD) == 4:
        print('Sorry, you lost!')
        break
