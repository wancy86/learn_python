#Python中的__new__和__init__

写了这么多的class，现在才知道还有个\_\_new\_\_方法

```python
class TestCls():
    """docstring for TestCls"""

    def __init__(self, name):
        print('init...')
        self.name = name

    def __new__(cls, name):
        print('new...')
        return super().__new__(cls)


c = TestCls("CooMark")
print(type(c))
print(c.name)
# new...
# init...
# <class '__main__.TestCls'>
# CooMark
```

###异同点

\_\_new\_\_和\_\_init\_\_有相同的参数，但是第一参数的意义和作用不一样

\_\_new\_\_ 用来创建实例，分配空间，返回的实例作为参数传递个\_\_init\_\_

\_\_init\_\_ 用来初始化实例，设置属性什么的

[这篇文章写的非常好, 戳这里...](http://www.jb51.net/article/48044.htm)

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
