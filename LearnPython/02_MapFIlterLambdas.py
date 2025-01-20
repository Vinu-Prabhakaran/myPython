import string


def squares(num):
    return num * num

def is_even(num):
    return num % 2 == 0

if __name__ == '__main__':
    print('Lets practice python map filter and lambdas')
    num_list=[1,2,3,4]
    print(list(map(squares,num_list)))
    print(list(filter(is_even,num_list)))
    ## Lets do the same with lambdas
    print(list(map(lambda n : n ** 2, num_list)))
    print(list(filter(lambda n: n % 2 == 0,num_list)))

    print(list(string.ascii_lowercase))