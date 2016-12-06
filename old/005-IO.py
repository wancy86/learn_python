print("----------------IO----------------")
# convert to string using repr() and str()
a=[x for x in range(10)]
a='[x for x in range(10)]'
a='1/7\n132'
print(str(a))
print(repr(a))

# 1.
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

# 2.
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

# str的对齐方法
# str.rjust()
# str.ljust()
# str.center()
# (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)
print('1'.rjust(5))
print('12'.rjust(5))
print('132'.rjust(5))
print('123456789'.rjust(5)[:5])
print('\n')

# str.zfill() 填充0
print('-100'.zfill(9))
print('4/09/2016'.zfill(10))
print('\n')

# str.format()
# '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
# 'We are the {} who say "{}!"'.format('knights', 'Ni')
print('Name:{}, age:{}'.format('Mark','29'))
print('Name:{0:2d}, age:{1:2d}'.format(123456,2929))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

# float 0:.3f
# int 0:3d 不到三位就前面补空格
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
print('{0:3d}'.format(12345))
# 
table = {'Sjoerd': 4127, 'Jack': 409800, 'Dcab': 7678002}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

# access dictionary
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ','Dcab: {0[Dcab]:d}'.format(table))
# use ** notation unpackage the dictionary
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# vars() returns a dictionary containing all local variables.
# print(vars())

# Reading and Writing Files¶
print('--------------Reading and Writing Files-----------------')
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
f=open('testfile.txt','r+',encoding='utf-8')

# read whole file
print(f.read())

print('--------------------')
# read whole file of 100 bytes 
f.seek(0) #back to the beginning
print(f.read(100))
print('--------------------')

# f.seek(-3) # Go to the 3rd byte before the end

# line by line
f.seek(0)
for line in f:
    print(line, end='')

print('---------read to list-----------')
# list(f) or f.readlines()
print('# 1')
f.seek(0)
l=list(f)
print(l)

print('# 2')
f.seek(0)
l=f.readlines()
print(l)

print('---------read to json-----------')
#f.close()
# import json
# x = object();
# json.dump(x, f)
# x = json.load(f)