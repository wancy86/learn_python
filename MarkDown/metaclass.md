#Python魔法 - MetaClass

>metaclass 
>>The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

metaclass是class的class，类的类 - 元类，那肯定最累了![](http://mat1.gtimg.com/www/mb/images/face/13.gif)，所有实例的创建都需要metaclass的参与. metaclass能拿到第一手的信息：
1. 类名
2. 父类集合
3. 类成员dict
然后想怎么改就怎么改，这就是当你看到某些class明明定义了xxx,可是运行时总是报错：没有xxx。
metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”，没有它你的calss也会抛未定义错误。

###使用metaclass来为类添加方法

通过修改metacalss，是创建的实例默认就有某些方法，这样是不是装逼过度？直接修改来的属性不就搞定了么![](http://mat1.gtimg.com/www/mb/images/face/32.gif).是的，但是总有些场景需要这么做。这里我们只能那个不是很实用的场景来看看metaclass是如何修改类的。
>按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass.

*. 任务：
    1. 给PythonProgrammer类添加一个play_cool method
    2. 去掉PythonProgrammer类的has_girlfriend![](http://mat1.gtimg.com/www/mb/images/face/5.gif), 好悲催

```python
class ProgrammerMetaClass(type):
    """docstring for Programmer"""
    def __new__(cls, name, bases, attrs):
        # 这里可以对类胡作非为的修改
        # 1.添加 play_cool method
        attrs['play_cool'] = lambda self: print('Programmers are cool...')
        # 2.删除属性
        if 'has_girlfriend' in attrs:
            del attrs['has_girlfriend']

        return type.__new__(cls, name, bases, attrs)


class PythonProgrammer(object, metaclass=ProgrammerMetaClass):
    """docstring for PythonProgrammer"""
    has_girlfriend = 0

    def __init__(self, language):
        super(PythonProgrammer, self).__init__()
        self.language = language


pp = PythonProgrammer('python')
pp.play_cool()
# Programmers are cool...
print(pp.has_girlfriend)

Traceback (most recent call last):
  File "D:\GitHub\learn_python\temp.py", line 78, in <module>
    print(pp.has_girlfriend)
AttributeError: 'PythonProgrammer' object has no attribute 'has_girlfriend'

print(PythonProgrammer.has_girlfriend)
Traceback (most recent call last):
  File "D:\GitHub\learn_python\temp.py", line 79, in <module>
    print(PythonProgrammer.has_girlfriend)
AttributeError: type object 'PythonProgrammer' has no attribute 'has_girlfriend'
```


