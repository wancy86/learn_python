print("----------------range----------------")

def test():
    print(0)
    pass

test()

# BEtter way use range
a = ['Mary', 'had', 'a', 'little', 'lamb']
for x in range(len(a)):
    print(x)

print("----------------range----------------")
# 
# range
# 
# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# python 2 get a xrange, python 3 combined them
print(range(0,10)) # will get: range(0,10)
print(list(range(5))) #but we can pint the list


print("----------------for----------------")
# when the for is exhaustion then run else
for x in range(1,10):
    print(x)
else:
    print('for exhaustion')

print("----------------function----------------")
# Fibonacci series to an arbitrary boundary:
# 1.
def Fibonacci(level):
    a,b=0,1
    while a<level:
        print(a,end=' ')
        a,b=b,a+b
        pass
Fibonacci(2000)

def my_function():
    '''
    this is function document literal string
    '''
    pass

print(my_function.__doc__)

# 2.


print("----------------list----------------")
# three ways to create a list
squares = []
for x in range(10):
    squares.append(x**2)
squares1 = list(map(lambda x: x**2, range(10)))
squares2 = [x**2 for x in range(10)]

# Generator
# two way to get a complex list
combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs2.append((x, y))

# That's awesome!!!
# open your imagination
L3=[(x,y,z) for x in range(4) for y in range(4) for z in range(4)]
print(L3)

# Bright to blind
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
# column to row
L4=[[row[i] for row in matrix] for i in range(4)]
print(L4)
# equivalent to:
L5 = []
for i in range(4):
    L5.append([row[i] for row in matrix])
# and equivalent to:
L6 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    L6_row = []
    for row in matrix:
        L6_row.append(row[i])
    L6.append(L6_row)
print(L6)

# but we get a built-in function zip(),LOL
print('using zip:')
L7=list(zip(*matrix))
print(L7)

# del function
print('del:')
a=[0,1,2,3,4,5,6,7,8,9]
print(a)

del a[0] 
print(a)

del a[2:4]
print(a)

del a[:] # pr use: del a
print(a)

print("----------------Tuples----------------")
print('5.3. Tuples and Sequences:')
# packing
x,y,z=4,5,6
t=x,y,z
print(t)
# unpacking 
t=1,2,3
x,y,z=t
print(x,y,z)

print("----------------Set----------------")
# A set is an unordered collection with no duplicate elements. 
# Curly braces{} or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};
#       the {} creates an empty dictionary

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) 
print('orange' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a) #{'c', 'a', 'r', 'd', 'b'}
print(b)
print('a-b:',a-b) # letters in a but not in b
print('a|b:',a|b) # letters in either a or b
print('a&b:',a&b) # letters in both a and b
print('a^b:',a^b) # letters in a or b but not both

#other way create set
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

print("----------------dictionary----------------")
# dictionaries are indexed by keys, which can be any immutable type
# It is best to think of a dictionary as an unordered set of key: value pairs
# the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}
# Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order (if you want it sorted, just use sorted(d.keys()) instead).
# To check whether a single key is in the dictionary, use the in keyword.
tel = {'jack': 4098, 'sape': 4139,'anne':13456,"xman":8888}
tel['guido'] = 4127
print(tel)
print('jack:',tel['jack'])
del tel['sape']
print('del sape:',tel)
print('list(tel.keys()):',list(tel.keys()))
print('sorted(tel.keys()):',sorted(tel.keys()))

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
d1=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d1)
d2={x: x**2 for x in (2, 4, 6)}
print(d2)
d3= dict(sape=4139, guido=4127, jack=4098)
print(d3)

print("----------------Looping Techniques----------------")
# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

# if null get other
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# Comparing Sequences
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

