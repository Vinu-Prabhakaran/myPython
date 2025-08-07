
def new_decorator(func_to_be_decorated):

    def wrap_func():
        print(f'New decoration before {func_to_be_decorated}')
        func_to_be_decorated()
        print(f'New decoration after {func_to_be_decorated}')
    return wrap_func

def decorate_me_func():
    print('I am the function to be decorated')

@new_decorator
def decorate_another_function():
    print('I am another function to be decorated')

if __name__ == '__main__':
    new_decorator(decorate_me_func)()
    #Now lets test with a decorator annotation
    print()
    decorate_another_function()