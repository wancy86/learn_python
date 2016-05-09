# 利用`@property`实现可控的属性操作
Python中没有访问控制符, 不像java之类的
```java
public class Person{
	private int x

	public int getAge(){
		return x
	}

	public void setAge(int age){
		this.x = age
	}
 }
```
###使用下划线的字段和对应的方法来限制字段的操作
开始很多人可能会想这么干
```python
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

###Python的`@property`装饰器
有了`@property`之后我们可方便的添加和设置属性
你可能需要：
* 验证属性值的合法性
* 设置只读属性
* 等等

```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

student = Student()
student.birth = 26  # setter

student.birth  # getter
student.age  # getter, age没有setter所以无法给age赋值 - 只读属性
```
