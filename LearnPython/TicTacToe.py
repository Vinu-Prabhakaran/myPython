import time
import itertools
from os import system, name


def clear_display_and_show_board(board):
    clear_screen()
    print('*** Current Board ***')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print('--|---|--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--|---|--')
    print(f'{board[0]} | {board[1]} | {board[2]}')


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def get_user_choice():
    choice = '#'

    while choice not in ['X', 'O']:
        choice = input('Please make your choice X or O ? ')
        if choice not in ['X', 'O']:
            print("Sorry! Wrong choice. Please pick X or O ")
    if choice == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def ask_player_move(marker, board):
    cell_chosen = False
    userinp = 'X'
    while not cell_chosen:
        userinp = input(f"Player {marker} - Enter the cell to be filled 1 to 9 :")
        if userinp.isdigit() and int(userinp) in range(1, 10) and board[int(userinp) - 1] == ' ':
            cell_chosen = True
        else:
            if not userinp.isdigit():
                print("Wrong choice !!! Please choose a number 1 to 9")
            elif int(userinp) not in range(1, 10):
                print("Wrong choice !!! Number should be 1 to 9")
            else:
                print("Wrong Choice!!! The cell is already occupied.")

    board[int(userinp) - 1] = marker
    return board


def check_board_full(board):
    return ' ' not in board


def win_check(board, mark):
    if board[0:3] == [mark] * 3 or \
            board[0:7:3] == [mark] * 3 or \
            board[2:9:3] == [mark] * 3 or \
            board[6:9] == [mark] * 3 or \
            board[3:6] == [mark] * 3 or \
            board[1:8:3] == [mark] * 3 or \
            board[0:9:4] == [mark] * 3 or \
            board[2:7:2] == [mark] * 3:
        return mark


if __name__ == '__main__':

    replay = "Y"
    # clear_display_and_show_board(board)
    ## Game starts This needs to be in loop until replay ON and borard is not full
    while replay.upper() == 'Y':
        clear_screen()
        print('Welcome to Tic-Tac-Toe')
        init_board = [' '] * 9
        # time.sleep(2)
        player1, player2 = get_user_choice()
        print("Player 1 " + player1)
        print("Player 2 " + player2)
        board = init_board
        won = '#'
        while not check_board_full(board) and won not in ['X', 'O']:
            clear_display_and_show_board(board)
            board = ask_player_move(player1, board)
            won = win_check(board, player1)
            clear_display_and_show_board(board)
            if not check_board_full(board) and won not in ['X', 'O']:
                board = ask_player_move(player2, board)
                won = win_check(board, player2)
                clear_display_and_show_board(board)

        if won in ['X', 'O']:
            print(f"Player {won} won!!!")
        else:
            print("It's a Draw!")
        replay = input("Press Y to play again ...")

    print("Thanks for playing ... Bye")
