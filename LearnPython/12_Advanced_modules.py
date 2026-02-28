from collections import Counter
import os

if __name__ == '__main__':

    l = 'qqqqbbbbqqqq'
    print(Counter(l).most_common()[0][0])

    print(os.getcwd())

    config={"name":"Vinu","age" :41}
    print(config["name"])