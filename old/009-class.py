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




# --------------------------------------------------------------------


# 3. 对象成员的私有性
# 在Python中是不支持私有变量的，但是有一个方式，可以让使客户端不能直接调用该变量：
# 对某个属性加一个双下划线的前缀，这样使得该属性会自动添加上一个_ClassName的前缀。
print('\r\n# 对象成员的私有性')
class SecretString:
    def __init__(self, plain_string):
        self.__plain_string = plain_string

    def get_plain_string(self):
        return self.__plain_string

s = SecretString('hello world')            

print('s.get_plain_string =', s.get_plain_string())

print('s._SecretString.__plain_string =', s._SecretString__plain_string) #自动添加的前缀 _SecretString

# print(s.__plain_string) #这个无法访问，会报错


# 2. 类的属性
# 值类型的类的属性，实例对象默认使用类的属性值，如果实例对象设置了该属性则使用自己的属性
print('\r\n# 值类型的类的属性')
class Human1(object):
    ancestor = 'dog'
    def __init__(self, name):
        super(Human1, self).__init__()
        self.name = name

Tom = Human1('Tom')
print('Tom.ancestor =',Tom.ancestor)

Tom.ancestor = 'Monkey'
print('Tom.ancestor =',Tom.ancestor)

Jim = Human1('Jim')
Jim.ancestor = 'Pig'
print('Jim.ancestor =',Jim.ancestor)

print('\r\n')
print('Tom.ancestor =',Tom.ancestor)
print('Jim.ancestor =',Jim.ancestor)
print('Human1.ancestor=',Human1.ancestor)


# 引用类型的类的属性
# 实例对象未设置属性时，使用类的属性，设置后就使用自己的
# 引用类型的类属性，如果实例对象重新指向新地址那么就不再和类属性共有了
print('\r\n# 引用类型的类的属性')
class Human2(object):
    ancestor = []
    def __init__(self, name):
        super(Human2, self).__init__()
        self.name = name

Tom = Human2('Tom')
print('Tom.ancestor =',Tom.ancestor)
Tom.ancestor.append('Tom')
print('Tom.ancestor =',Tom.ancestor)

Jim = Human2('Jim')
print('Jim.ancestor =',Jim.ancestor)
Tom.ancestor.append('Jim')
print('Jim.ancestor =',Jim.ancestor)

print('Tom.ancestor =',Tom.ancestor)
print('Jim.ancestor =',Jim.ancestor)
print('Human2.ancestor =',Human2.ancestor)

print('\r\n# 引用类型的类的属性2')
class Human3(object):
    ancestor = ['Dog']
    def __init__(self, name):
        super(Human3, self).__init__()
        self.name = name

Tom = Human3('Tom')
Tom.ancestor=[]
Tom.ancestor.append('Tom')
print('Tom.ancestor =',Tom.ancestor)

Jim = Human3('Jim')
Jim.ancestor.append('Jim')
print('Jim.ancestor =',Jim.ancestor)
print('\n')
print('Tom.ancestor =',Tom.ancestor)
print('Jim.ancestor =',Jim.ancestor)
print('Human3.ancestor =',Human3.ancestor)

# SublimeCodeIntel - 智能提示插件

# 简单继承
# 1. 所有的class全部直接或者间接的继承与object.
# 2. super()方法可以用来访问父类的方法，如果子类拥有和父类同名的方法，则子类会重写父类的方法。
# 3. 类的引用类型的成员变量定义后，所有的子子孙孙共享一个成员变量

# 简单继承
print('\r\n# 简单继承')
class Contact(object):
    # 引用类型的类级别成员变量
    contact_list = []
    def __init__(self, name, email, telephone):
        # 值类型的对象级别成员变量
        self.name = name
        self.email = email
        self.telephone = telephone

        Contact.contact_list.append(self)    

Contact_A = Contact('Tom', 'tom@gmail.com', 123456)
Contact_B = Contact('Lucy', 'lucy@gmail.com', 123457)

print('Contact:')
for c in Contact.contact_list:
    print(c.name)        


class Friend(Contact):
    friend_list = []
    # 重写父类的方法
    def __init__(self, name, email, telephone, age):
        # 调用父类的方法
        super(Friend, self).__init__(name, email, telephone)
        self.age = age
        Friend.friend_list.append(self)
                    
Friend_A = Friend('Jack', 'jack@gmail.com', 123458, 22)
Friend_B = Friend('Jim', 'jim@gmail.com', 123459, 23)    

# It is a little strange that the child class has quite the same contact_list
print(Contact.contact_list)    
print(Friend.contact_list)

print('Friends:')

for f in Friend.friend_list:
    print(f.name, f.age)

# Python的实现多态的方式，将和其他高级语言有很大的差别，Python本身弱类型，所以在Pyhon中实现多态似乎没有太大的意义。
print('\r\n# 多态')
class AudioPlayer(object):
    def __init__(self, file_name):
        super(AudioPlayer, self).__init__()
        if not file_name.endswith(self.ext):
            raise Exception("Invalid file format")
        self.file_name = file_name

class MP3Player(AudioPlayer):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.file_name))

class WAVPlayer(AudioPlayer):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.file_name))            

mp3_player = MP3Player("xx.mp3")

wav_player = WAVPlayer("yy.wav")

mp3_player.play()
wav_player.play()

# 1. 简单多重继承：
# 多重继承一个比较麻烦的问题就是父类的初始化的问题，下面这个例子算是一般比较常见的方式。
# 但是这种方式存在着一个问题，那就是object的初始化函数将运行两次，一般情况下这不会产生什么问题，
# 但是有时候可能会引起设计上的致命缺陷。
print('\r\n# 简单多重继承：')
class Mother(object):
    def __init__(self, first_name):
        self.first_name = first_name

class Father(object):
    def __init__(self, last_name):
        self.last_name = last_name

class Child(Mother, Father):
    def __init__(self, first_name, last_name):
        Mother.__init__(self, first_name)
        Father.__init__(self, last_name)

Tom = Child('Tom', 'Jim')    

print(Tom.first_name, Tom.last_name)


#  下面的例子体现了父类初始化两次的例子，一般情况下，这并不是太常见
print('\r\n# 多重继承-基类__init__被执行两次：')
class BaseClass(object):
    def __init__(self, age):
        self.age = age
        print("BaseClass' __init__ is invoked.")

class Mother(BaseClass):
    def __init__(self, first_name, age):
        BaseClass.__init__(self, age)
        self.first_name = first_name

class Father(BaseClass):
    def __init__(self, last_name, age):
        BaseClass.__init__(self, age)
        self.last_name = last_name

class Child(Mother, Father):
    def __init__(self, first_name, last_name, age):
        Mother.__init__(self, first_name, age)
        Father.__init__(self, last_name, age)

Tom = Child('Tom', 'Yao', 12)    

print(Tom.first_name, Tom.last_name)

# 2. 使用字典参数来实现，爷爷类只被调用一次
print('\r\n# 多重继承-字典参数来实现-基类__init__执行一次：')
class BaseClass(object):
    def __init__(self, age = '', **kwargs):
        self.age = age
        print("BaseClass' __init__ is invoked.")

class Mother(BaseClass):
    def __init__(self, first_name = '', **kwargs):
        super().__init__(**kwargs)
        self.first_name = first_name
        print("Mother's __init__ is invoked.")

class Father(BaseClass):
    def __init__(self, last_name = '', **kwargs):
        super().__init__(**kwargs)
        self.last_name = last_name
        print("Father's __init__ is invoked.")

class Child(Mother, Father):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

Tom = Child(**{"age":21, "first_name":"Miles", "last_name":"Yao"})    

print(Tom.first_name, Tom.last_name)

print('\n弄清楚super()的原理很重要...')

