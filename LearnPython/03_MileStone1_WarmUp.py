from os import system,name
# Set TERM=xterm-256color in run config env variable

def get_user_input():
    valid_input = False
    inp = ''
    while not valid_input:
        inp = input('Enter a number (1-9) :')
        if inp.isdigit() and int(inp) in range (0,10):
            valid_input = True

    return int(inp)


def update_list(list_data, user_inp):
    new_data = input("Please enter replacement value :")
    list_data[user_inp - 1] = new_data
    return list_data


def clear_console():
    if name == 'win':
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':

    repeat = 'Y'
    list_data = [' '] * 10

    while repeat == 'Y':
        clear_console()
        user_inp = get_user_input()
        print(f"User choice is : {user_inp}")
        print(f'Updated List : {update_list(list_data, user_inp)}')
        repeat = input("Play again ? ('y/n') :")