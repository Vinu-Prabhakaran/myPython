
if __name__ == '__main__':
    name = 'VinuPrabhakaran'
    names = ['Vinu','Ramya','Ameya',"Aditi"]
    # Quick Debugging
    print(f'{name = }')
    print(f'{len(names) = }')
    print(f'{[name for name in names] =}')
    # Print args
    print(*name) # default separator space
    print(*name,sep='')
    print(*names,sep=',',end='.\n')
    # Iterating
    f,*_,l = 'Vinu' # Read string as a list
    print(f,l)
    first,*_ = names
    print(*_,sep=',')
    # Combining sets with union operator
    a:set[int] = {1,2,3}
    b = {3, 4, 5}
    c:set[int] = a | b
    print(f'{c = }')
    # Combining dicts
    d1 = {'k1':1,'k2':2,'k3':3}
    d2 = {'k2':2,'k4':4,'k5':5}
    print(f'{d1|d2 =}')
    # Looping with else clause
    for person in names:
        print(f'{person = }')
    else:
        print('All names are printed.') # Executed if loop completed without a break
    # Comprehension
    print(f'{[num for num in range(3)] = }') # List (stores everything in RAM)
    print({num for num in [0, 0, 1, 1, 3, 2, 2]}) # Set
    print({k:v for k,v in [('k1','v1'),('k2','v2')]}) # Dictionary
    print((num for num in range(3))) # Generator expression (computes on the fly)

    # Unpacking **kwargs
    settings = {'sep':',','end':'!\n'}
    print(*names,**settings)

    # Reusable slices
    first_three = slice(0,2)
    reverse = slice(None,None,-1)
    print(f'{name[first_three] = }')
    print(f'{name[reverse] = }')

    # Multiple assignments
    a, b, c = 10, 12, 5

    # Enumerating in loops
    print('Enumerating in loops')
    for i, value in enumerate(names):
        print(i,value)

    # Enumerate with start
    print('Enumerate with start')
    for i, value in enumerate(names, start= 1): # starts at 1 .Start num can be negative as well.
        print(i,value)

    # Safely retrieve dict values
    print('Safely retrieve dict values')
    print(f'{settings.get('sep') = }')
    print(f'{settings.get('start',':') = }') # Exit without exception for an unknown key. Optional default

    # Conditional one-liners
    volume = 0.6
    print(f'{'loudness' if volume > .6 else 'silent' = }')

    # max and min with key
    print('Max and Min with key')
    students = [
        {'name':'Bob','score':50},
        {'name':'Sarah','score':75},
    ]
    print(max(students, key=lambda s:s['score']))
    print(min(students, key=lambda s:s['score']))