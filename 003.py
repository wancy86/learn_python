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
