# 使用\_\_slots\_\_

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的\_\_slots\_\_变量，来限制该class实例能添加的属性：


```python
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
```
然后，我们试试：

```python
s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
s.score = 99  # 绑定属性'score'
```
```
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
AttributeError:
    'Student' object has no attribute 'score'
```
由于'score'没有被放到\_\_slots\_\_中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用\_\_slots\_\_要注意，\_\_slots\_\_定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
```python
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
```

除非在子类中也定义\_\_slots\_\_，这样，子类实例允许定义的属性就是自身的\_\_slots\_\_加上父类的\_\_slots\_\_。
