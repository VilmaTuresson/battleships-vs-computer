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
            if row in '12345678'
            row = int(row)
            break
        except ValueError:
            print("That's not a valid number, please try again")

    while True:
        try:
            column = input('Enter a number between 1 - 8: ')
            if column in '12345678'
            column = int(row)
            break
        except ValueError:
            print("That's not a valid number, please try again")
    return row, column




#def set_user_ships(board):
    #user_row = input('enter a number between 1 - 8: ')
    #user_collumn = input('enter a number between 1 - 8: ')
    #while board[user_row][user_collumn] == '@':
        #user_row = input('enter a number between 1 - 8: ')
        #user_collumn = input('enter a number between 1 - 8: ')
    #board[user_row][user_collumn] = '@'


def create_computer_ships():
    pass


def count_sunken_ships():
    pass

