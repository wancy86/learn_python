#Python中的__new__和__init__

<div style="background-color: #69C3EC"> </div>

写了这么多的class，现在才知道还有个\_\_new\_\_方法, 那么它和\_\_init\_\_有什么区别呢？

```python
class TestCls():
    """docstring for TestCls"""

    def __init__(self, name):
        print('init')
        print(self)
        print(type(self))
        self.name = name

    def __new__(cls, name):
        print('new')
        print(cls)
        print(type(cls))
        return super().__new__(cls)

c = TestCls("CooMark")

# new...
# <class '__main__.TestCls'>
# <class 'type'>

# init...
# <__main__.TestCls object at 0x02201130>
# <class '__main__.TestCls'>

```

###异同点
<hr>
1. 参数
    * \_\_new\_\_的第一个占位参数是class对象
    * \_\_init\_\_的第一个占位参数是class的实例对象
    * 其他的参数应一致
2. 作用
    * \_\_new\_\_ 用来创建实例，在返回的实例上执行\_\_init\_\_，如果不返回实例那么\_\_init\_\_将不会执行
    * \_\_init\_\_ 用来初始化实例，设置属性什么的



###利用\_\_new\_\_我们能做哪些牛逼的事情？
<hr>
>Python文档
>>object.__new__(cls[, ...]) 
>>Called to create a new instance of class cls. __new__() is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of __new__() should be the new object instance (usually an instance of cls).
>>
>>Typical implementations create a new instance of the class by invoking the superclass’s __new__() method using super(currentclass, cls).__new__(cls[, ...]) with appropriate arguments and then modifying the newly-created instance as necessary before returning it.
>>
>>If __new__() returns an instance of cls, then the new instance’s __init__() method will be invoked like __init__(self[, ...]), where self is the new instance and the remaining arguments are the same as were passed to __new__().
>>
>>If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked.
>>
>>__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.
>>

依照Python官方文档的说法，\_\_new\_\_方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的[metaclass](http://www.cnblogs.com/wancy86/p/python_meteclass.html)。

+ *继承不可变class* [`参考`](http://www.jb51.net/article/48044.htm)

假如我们需要一个永远都是正数的整数类型，通过集成int，我们可能会写出这样的代码

```python
class PositiveInteger(int):

    def __init__(self, value):
        super().__init__(self, abs(value))

i = PositiveInteger(-3)
print(i)
# # TypeError: object.__init__() takes no parameters


class PositiveInteger(int):

    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))
i = PositiveInteger(-3)
print(i)
# 3
```

+ *用\_\_new\_\_来实现单例*

```python
class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
obj1 = Singleton()
obj2 = Singleton()
obj1.attr1 = 'value1'
print( obj1.attr1, obj2.attr1)
print( obj1 is obj2)
```

<div style="background-color: #69C3EC"> </div>


