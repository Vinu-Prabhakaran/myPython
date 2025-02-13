from os import system,name

def add(num1,num2):
    print(f'Sum of {num1} & {num2} is {num1 + num2}')

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def print_square_of_integer():
    while True:
        try:
            num = int(input('Enter an integer :'))
            print(f'Square of {num} is {num ** 2}')
        except:
            clear_screen()
            print('Please provide a valid input')
            continue
        else:
            print('Square function executed without errors')
            break
        finally:
            print('Thank You!')



if __name__ == '__main__':
    try:
        add(10,'A')
    except TypeError:
        print('Looks like there is an error')
    else:
        print('No Error!')
    finally:
        print('Addition is complete')

    print_square_of_integer()
