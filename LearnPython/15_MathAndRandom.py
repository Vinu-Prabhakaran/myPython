import math
import random
from math import log,e,pi,radians,degrees
import pdb

if __name__ == '__main__':
    print(pi)
    print(degrees(pi)) # 180
    print(log(e))
    print(radians(90)) # pi/2
    print(log(100,10))
    print(math.sin(radians(90))) # Argument should be in radians
    print(math.sin(pi/2))

    ## Random
    my_list = list(range(0,20))
    # pdb.set_trace() # Set trace q to quit from trace
    print(my_list)
    random.shuffle(my_list)
    print(f'Shuffled list is : {my_list}')
    print(f'Random integer including 0 and 100 is {random.randint(0, 100)}')

    print(f'Random choice is {random.choice(my_list)}')
    print(f'Random choice of 10 items is {random.choices(population=my_list,k=10)}') # With replacement (may repeat)
    print(f'Random choice of 10 items is {random.sample(population=my_list,k=10)}') # Without replacement (no repeat)

