#Python - 动手写个ORM

###任务：
1. 模拟简单的ORM - Object Relational Mapping
2. 为model添加create方法

代码很简单，直接上

###字段类型类
```python

class Field(object):
    """docstring for Field"""

    def __init__(self, field_type, default, max_length,  * arg):
        super().__init__()
        self.default = default
        self.max_length = max_length
        self.field_type = field_type


class CharField(Field):
    """docstring for CharField"""

    def __init__(self, max_length=100, *arg):
        super().__init__('char', '', max_length)


class DateField(Field):
    """docstring for DateField"""

    def __init__(self, default='now', *arg):
        if(default == 'now'):
            from datetime import datetime
            self.default = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            self.default = default
        super().__init__('datetime', self.default, None)


class IntField(Field):
    """docstring for IntField"""

    def __init__(self, default=0, *arg):
        super().__init__('int', 0, 8)

```


###很关键的MetaClass
```python

class ModelMetaClass(type):
    """docstring for ModelMetaClass"""

    def __new__(cls, name, bases, attrs):
        print('2. ModelMetaClass __new__')
        mapping = {}
        # mapping = dict()
        for k, v in attrs.items():
            if(isinstance(v, Field)):
                mapping[k] = v
        for k, v in mapping.items():
            del attrs[k]

        # 挂到实例上
        # attrs['mapping'] = mapping
        cls_obj = type.__new__(cls, name, bases, attrs)

        # 这里为了测试效果简单的将需要的信息添加到类的动态属性上
        cls_obj.mapping = mapping
        cls_obj.table = name

        return cls_obj

# 如果子类中指定metaclass那么必须从父类的meta继承以维持正确的调用顺序
class NewsMetaClass(ModelMetaClass):
    """docstring for NewsMetaClass"""
    print('1. NewsMetaClass __new__')

    def __new__(cls, name, bases, attrs):
        # do anything you want

        # attrs['create'] = NewsMetaClass.create

        clsobj = super().__new__(cls, name, bases, attrs)
        return clsobj
```

###Model类, 注意`metaclass`的设定

```python        
class Model(object, metaclass=ModelMetaClass):
    """docstring for Model"""

    def __init__(self, *arg):
        super(Model, self).__init__()
        self.arg = arg

    @classmethod
    def create(cls, **kwargs):
        fields = []
        params = []
        args = []

        for k, v in cls.mapping.items():
            fields.append(k)
            params.append('?')
            args.append(kwargs[k])

        sql = 'insert into %s (%s) values(%s)' % (cls.table, ','.join(fields), ','.join(params))
        param = ','.join(args)
        print('SQL: %s' % (sql))
        print('args: %s' % param)
        # exec the sql


class News(Model, metaclass=NewsMetaClass):
    """docstring for News"""
    title = CharField(max_length=100)
    content = CharField(max_length=500)
    publish_date = DateField(default="now")
    read_count = IntField(default=0)
```

###测试效果
```python
from datetime import datetime
News.create(title='test', content='asdf', read_count='0', publish_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# SQL: insert into News (publish_date,content,title,read_count) values(?,?,?,?)
# args: 2016-05-16 22:39:54,asdf,test,0

```

参考：[使用元类](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000)
