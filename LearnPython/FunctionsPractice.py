from random import shuffle


def hello_func(name):
    print(f'Hello {name}')

def checkeven_list(num_list):
    '''
    Return True if any number is Even in the list
    :param num_list:
    :return:
    '''
    for num in num_list:
        if (num % 2 == 0):
            return True
    return False

def enter_even_number():
    inp = 1
    while inp % 2 != 0:
        inp = int(input('Enter an even number'))
    return inp

def give_even_list(num_list):
    '''
    Return all Even in the list
    :param num_list:
    :return:
    '''
    even_list=[]
    for num in num_list:
        if (num % 2 == 0):
            even_list.append(num)
    return even_list


def shuffle_list(num_list):
    shuffle(num_list)
    return num_list


def add_var_numbers(*args):
    return sum(args)


def test_kwargs(*args,**kwargs):
    print(f"Age of {kwargs['p1']} is {args[0]}")
    print(f"Age of {kwargs['p2']} is {args[1]}")

def lesser_of_two_evens(n1,n2):
   print('lesser_of_two_evens')
   if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1,n2)
   else:
       return max(n1,n2)

def animal_crackers(word):
    print('animal_crackers')
    parts=word.split()
    if len(parts) == 2 and parts[0][0] == parts[1][0]:
        return True
    return False


def makes_twenty(n1, n2):
    '''
    MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
    or if one of the integers is 20. If not, return False
    :param n1:
    :param n2:
    :return:
    '''
    print('makes_twenty')
    if type(n1) == int and type(n2) == int:
        return n1 == 20 or n1 + n2 == 20
    return False


def old_macdonald(name):
    '''
    OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    :param name:
    :return:
    '''
    print('old_macdonald')
    return name[:3].capitalize()+name[3:].capitalize()


def master_yoda(input):
    '''
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    :param input:
    :return:
    '''
    print('master_yoda')
    return ' '.join(input.split()[::-1])


def almost_there(num):
    '''
    ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    :param num:
    :return:
    '''
    print(f'almost_there - {num}')
    return abs(100 - num) <= 10 or abs(num - 200) <= 10


def has_33(num_list):
    '''
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    :param num_list:
    :return:
    '''
    print(f'has_33({num_list})')
    for idx in range(0,len(num_list) - 1):
        if (num_list[idx] == 3 and num_list[idx + 1] == 3):
            return True
    return False


def paper_doll(word):
    '''
    PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    :param word:
    :return:
    '''
    print(f'paper_doll({word})')
    result = ''
    for l in word:
        result += l*3
    return result


def blackjack(n1, n2, n3):
    '''
    BLACKJACK: Given three integers between 1 and 11,
    if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    :param n1:
    :param n2:
    :param n3:
    :return:
    '''
    print(f'blackjack({n1}, {n2}, {n3})')
    total = n1 + n2 + n3
    if total <= 21:
        return total
    elif total <= 31 and [n1,n2,n3].__contains__(11):
        return total - 10
    else:
        return 'BUST'


def summer_69(num_array):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6 and extending to the next 9
    (every 6 will be followed by at least one 9). Return 0 for no numbers.
    :param num_array:
    :return:
    '''
    print(f'summer_69({num_array})')
    # found_6 = False
    # total = 0
    # discount = 0
    # for num in num_array:
    #     total += num
    #     if (num == 6 and not found_6):
    #         found_6 = True
    #         discount += num
    #         continue
    #     if found_6 and num != 9:
    #         discount += num
    #         continue
    #     if found_6 and num == 9:
    #         discount += num
    #         total -= discount
    #         discount = 0
    #         continue
    # return total
    add = True
    total = 0
    for num in num_array:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num == 9:
                add = True
            else:
                break
    return total


def spy_game(num_list):
    '''
    SPY GAME: Write a function that takes in a list of integers
    and returns True if it contains 007 in order
    :param int_list:
    :return:
    '''
    print(f'spy_game({num_list})')
    code=[0,0,7,'x']
    for num in num_list:
        if num == code[0]:
            code.remove(num)
    return len(code) == 1


def count_primes(num):
    '''
    COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
    :param num:
    :return:
    '''
    print(f'count_primes({num})')
    primes=[]
    if num >= 2:
        primes.append(2)
    for num in range(3,num+1,2):
        for prime in primes:
            if num % prime == 0:
                break # Check no further divisibility by the prime list available so far
        else:
            primes.append(num)
    return len(primes),primes


def print_big(ch):
    '''
    PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter¶
    print_big('a')

    out:   *
          * *
         *****
         *   *
         *   *

    HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
    For purposes of this exercise, it's ok if your dictionary stops at "E".
    :param ch:
    :return:
    '''
    print(f'print_big({ch})')
    patterns = ['*     ','  *  ','**** ',' ****','*****',' * * ','*   *']
    code_dict={'A':[1,5,4,6,6],
               'B':[2,6,4,6,2],
               'C':[3,0,0,0,3],
               'D':[2,6,6,6,2],
               'E':[4,0,2,0,4],
               }
    for indx in code_dict[ch.upper()]:
        print(patterns[indx])

if __name__ == '__main__':
    print('Lets practice functions')
    hello_func('Vinu')
    num_list=[1,3,4,7,9]
    print(f'List - {num_list} : {checkeven_list(num_list)}')
    print(f'EvenList from {num_list} is {give_even_list(num_list)}')
    # num = enter_even_number()
    #print(f'You entered {num}')
    print(f'List - {num_list} : \nShuffled:{shuffle_list(num_list)}')
    print(f'Sum - {add_var_numbers(4,3,5,6)}')
    test_kwargs(40,37,p1='Vinu',p2='Ramya')

    print('abcd'.join(('1','2','3')))
    ## Test Function Exercises
    print(lesser_of_two_evens(2,4))
    print(lesser_of_two_evens(2, 5))

    print(animal_crackers('Levelheaded Llama'))
    print(animal_crackers('Crazy Kangaroo'))

    print(makes_twenty(20,10))
    print(makes_twenty(12,8))
    print(makes_twenty(21,10))

    print(old_macdonald('macdonald'))

    print(master_yoda('I am home'))

    print(almost_there(90))
    print(almost_there(104))
    print(almost_there(150))
    print(almost_there(209))

    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(has_33([3 , 1, 3]))

    print(paper_doll('Hello'))
    print(paper_doll('Mississippi'))

    print(blackjack(5,6,7))
    print(blackjack(9,9,9))
    print(blackjack(9,9,11))

    print(summer_69([1, 3, 5]))
    print(summer_69([4, 5, 6, 7, 8, 9]))
    print(summer_69([2, 1, 6, 9, 11]))

    print(spy_game([1,2,4,0,0,7,5]))
    print(spy_game([1,0,2,4,0,5,7]))
    print(spy_game([1,7,2,0,4,5,0]))
    
    print(count_primes(1000))

    for ch in 'abcde': print_big(ch)