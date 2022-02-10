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

