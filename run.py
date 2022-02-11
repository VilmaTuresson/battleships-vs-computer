from random import randint


player_board = [[' '] * 8 for i in range(8)]
player_guess_board = [[' '] * 8 for i in range(8)]
computer_board = [[' '] * 8 for i in range(8)]
computer_guess_board = [[' '] * 8 for i in range(8)]


def print_board(board):
    """
    Function to loop out a grid
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
            row = input('Enter a number between 1 - 8: ')
            if row in '12345678':
                row = int(row)
            break
        except ValueError:
            print("That's not a valid number, please try again")

    while True:
        try:
            column = input('Enter a number between 1 - 8: ')
            if column in '12345678':
                column = int(row)
            break
        except ValueError:
            print("That's not a valid number, please try again")
    return row, column


def set_user_ships(board):
    for ship in range(4):
        print('Enter coordinates to set out your battleships!')
        user_row, user_column = get_user_input()
        while board[user_row][user_column] == '@':
            print('You have already placed a ship on these coorinates')
            user_row, user_column = get_user_input()
        board[user_row][user_column] = '@'

def create_computer_ships(board):
    """
    Function to get two random intergers to place out a ship and trying again if there is a ship places there already.
    """
    for ship in range(4):
        computer_row = randint(0, 8)
        computer_column = randint(0, 8)
        while board[computer_row][computer_column] == '@':
            computer_row = randint(0, 8)
            computer_column = randint(0, 8)
        board[computer_row][computer_column] = '@'
    


def count_sunken_ships():
    """
    Function to increment the sunken_ships variable when computer or user hits a ship.
    """
    sunken_ships = 0
    for row in board:
        for collumn in row:
            if sunken_ships == '*':
                sunken_ships += 1
        return sunken_ships

