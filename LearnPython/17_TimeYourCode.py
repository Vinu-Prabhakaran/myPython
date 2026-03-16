import shutil
import time
import timeit


def generate_series_01(user_input):
    my_list=[str(num) for num in range(1,user_input+1)]
    return my_list

def generate_series_02(user_input):
    my_list=list(map(str,range(1,user_input+1)))
    return my_list

if __name__ == '__main__':
    try:
        user_input = int(input("Enter a number :"))
        start_time = time.time()
        generate_series_01(user_input)
        end_time = time.time()
        print(f'Time taken by func1 - {end_time - start_time}')
        start_time = time.time()
        generate_series_02(user_input)
        end_time = time.time()
        print(f'Time taken by func2 - {end_time - start_time}')

    except:
        print('Not a number!')