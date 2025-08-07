
def fib_series_one(n):
    res = 0
    a = 1
    b = 1
    for _ in range(n):
        yield res
        res = a
        a = b
        b += res

def fib_series(n):
    a = 0
    b = 1
    for num in range(n):
        yield a
        a,b = b, a+b


def create_cubes(n):
    for num in range (n):
        yield num ** 3

if __name__ == '__main__':

    for e in fib_series(6):
        print(e)

    for x in create_cubes(10):
        print(x)
