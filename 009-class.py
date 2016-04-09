print("----------------Classes----------------")
print('Scopes and Namespaces Example---------------')
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

print('------------------class---------')
class Dog:

    kind = 'canine'         # class variable shared by all instances
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
    def add_trick(self, trick):
        self.tricks.append(trick)

dog=Dog('mydog')
print(dog.kind)
print(dog.name)

# Correct design of the class should use an instance variable instead:
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


class Cat(Dog):
    """docstring for Cat"""
    def __init__(self, arg):
        super(Cat, self).__init__(arg)
        self.arg = arg
        
cat=Cat('miao...miao...')
print(cat.name)

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
# Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

class Animum():
    """docstring for Animum"""
    def __init__(self, arg):
        super(Animum, self).__init__()
        self.arg = arg
        self.skill=arg[1]
        
class Duck(Dog,Animum):
    """docstring for Duck"""
    def __init__(self, arg):
        super(Duck, self).__init__(arg)
        self.arg = arg
        
duck=Duck(['Duck Tang','eat'])
print(duck.name)


# private variable
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

mapsub = MappingSubclass({x:x**2 for x in range(10)})
print(mapsub.items_list)

# Odds and Ends
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# Iterators
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char,end=' ')


# Generators
# yield 
# What makes generators so compact is that the __iter__() and __next__() methods are created automatically.
# Another key feature is that the local variables and execution state are automatically saved between calls.
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# Generator Expressions
sum(i*i for i in range(10))                 # sum of squares
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
# unique_words = set(word  for line in page  for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

