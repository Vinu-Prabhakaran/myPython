
if __name__ == '__main__':
    print("This is the main file for Python Basics")
    myVar = 'VinuPrabhakaran'
    print('Reverse String :'+ myVar[::-1])
    #Tuple unpacking
    print("Tuple unpacking")
    tup = ((1,'A'),(2,'B'),(3,'C'))
    for a,b in tup:
        print(f'{a} : {b}')
    #Dictionary unpacking
    print("Dictionary unpacking")
    myDict = {'k1':1,'k2':2,'k3':3}
    for key,value in myDict.items():
        print(f'{key} : {value}')
