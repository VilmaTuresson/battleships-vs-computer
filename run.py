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


def get_user_input():
    """
    Functions to get user input for setting and guessing locations.
    """
    while True:
        try:
            row = input('Select a row between 1 - 8: \n')
            if row in '12345678':
                row = int(row) - 1
                break
        except ValueError:
            print("That's not a valid number, please try again")

    while True:
        try:
            column = input('Select a column between 1 - 8: \n')
            if column in '12345678':
                column = int(column) - 1
                break
        except ValueError:
            print("That's not a valid number, please try again")
    return row, column


def set_user_ships(board):
    """
    Function calling the get_user_input function to place out user ships.
    """
    print('Enter coordinates to set out 4 battleships!')
    for ship in range(4):
        user_row, user_column = get_user_input()
        while board[user_row][user_column] == '@':
            print('You have already placed a ship on these coorinates')
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
            if sunken_ships == '*':
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
        print('You sank all your oppnents ships!')
        break

    while True:
        row, column = randint(0, 7), randint(0, 7)
        if COMPUTER_GUESS_BOARD[row][column] == '*':
            row, column = randint(0, 7), randint(0, 7)
        elif PLAYER_BOARD[row][column] == '-':
            row, column = randint(0, 7), randint(0, 7)
        elif PLAYER_BOARD[row][column] == '@':
            PLAYER_BOARD[row][column] = '*'
            print('Your opponent sank one of you ships!')
            #print_board(COMPUTER_GUESS_BOARD)
            break
        else:
            PLAYER_BOARD[row][column] = '-'
            break
    if count_sunken_ships(COMPUTER_GUESS_BOARD) == 4:
        print('Sorry, you lost!')
        break
