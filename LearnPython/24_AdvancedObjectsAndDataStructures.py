from six import iteritems, iterkeys, itervalues, viewitems

if __name__ == '__main__':
    # Advanced Numbers
    print(hex(15)) # Hex value
    print(bin(10)) # Binary value
    print(pow(4,3)) # 4 ** 3
    print(pow(4,3,3)) # (4 ** 3) % 3

    # Advanced Strings
    word = 'sample word to test'
    print(word.capitalize()) # First letter capitalize
    print(word.title()) # Capitalize first letter of each word
    print(word.upper())
    print(word.lower())
    print(word.count('t')) # Count of 't'
    print(word.find('t')) # First occurrence
    print(word.isalnum())
    print(word.isalpha())
    print(word.islower())
    print(word.isupper())
    print(word.isspace())
    print(word.startswith('s'))
    print(word.endswith('d'))
    print(word.split('t')) # Splits at every instance of split string
    print(word.partition('t')) # Returns a 3 item list - Part before first instance, partition string, part after first instance

    # Advanced Sets
    print('Advanced Sets')
    s = set()
    s.add(1)
    s.add(2)
    s.add(2)
    print(s)
    # s.clear() # Clears set
    # print(f'After s.clear() : {s}')
    sc = s.copy()
    print(f'Copy of s : {sc}')
    s.add(4)
    print(f's.difference(sc) : {s.difference(sc)}')
    s1 = {1,2,3,4}
    s2 = {3,4,5,6}
    print(f's1 : {s1}')
    print(f's2 : {s2}')
    s1.difference_update(s2) # updates s1 after removing common elements
    print(f's1.difference_update(s2) : {s1}')
    print(f's : {s}')
    s.discard(2)
    print(f's.discard(2) : {s}')
    s1.add(3)
    s1.add(4)
    print(f's1 : {s1}')
    print(f's2 : {s2}')
    print(f's1.intersection(s2) : {s1.intersection(s2)}')
    # s1.intersection_update(s2) # Updates s1 with result of intersection
    s1.isdisjoint(s2) # True if there is a null intersection
    s1.issuperset(s2) # True if s1 is a superset of s2
    s1.issubset(s2) # True if s1 is a subset of s2
    print(f's1.symmetric_difference(s2) : {s1.symmetric_difference(s2)}') # Returns set with elements only in one of the sets
    s1.union(s2) # Union from both sets
    s1.update(s2) # Updates s1 as union result

    # Advanced Dictionaries
    print('Advanced Dictionaries')
    d = {'k1': 1,'k2':2}
    print({x:x**2 for x in range(0,4)}) # Dictionary comprehension
    print(f'Dictionary iteration')
    for i in iteritems(d):
        print(i) # Returns tuples of entries

    for i in iterkeys(d):
        print(i) # Returns keys

    for i in itervalues(d):
        print(i) # Returns values

    print(viewitems(d)) # Similarly viewkeys(d) and viewvalues(d)
    for i in viewitems(d):
        print(i)

    # Advanced Lists
    print('Advanced Lists')
    l = [1,2,3,4,1]
    print(f'List l : {l}')
    print(f'l.count(1) :{l.count(1)}')
    # Difference between append and extend
    l.append([5,6])
    print(f'l.append([5,6]) gives : {l}')
    l.extend([8,9])
    print(f'l.extend([8,9]) gives {l}')
    print(f'l.index(1) : {l.index(1)}') # index of first occurrence
