

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


class ModelMetaClass(type):
    """docstring for ModelMetaClass"""

    def __new__(cls, name, bases, attrs):
        print('2. ModelMetaClass __new__')
        # mapping = {}
        # # mapping = dict()
        # for k, v in attrs.items():
        #     if(isinstance(v, Field)):
        #         # print('mapping:%s=>%s' % (k, v))
        #         mapping[k] = v
        #         # del attrs[k]
        #         # RuntimeError: dictionary changed size during iteration
        # for k, v in mapping.items():
        #     del attrs[k]

        # # attrs['save']=lambda self:self.
        # fields = []
        # params = []
        # args = []
        # for k, v in mapping.items():
        #     fields.append(k)
        #     params.append('?')
        #     # args.append(getattr)
        # attrs['__mapping__'] = mapping
        mapping = {}
        for k, v in attrs.items():
            if(isinstance(v, Field)):
                mapping[k] = v
        for k, v in mapping.items():
            del attrs[k]

        cls_obj = type.__new__(cls, name, bases, attrs)
        return cls_obj


class Model(object, metaclass=ModelMetaClass):
    """docstring for Model"""

    def __init__(self, *arg):
        super(Model, self).__init__()
        self.arg = arg


class NewsMetaClass(ModelMetaClass):
    """docstring for NewsMetaClass"""
    print('1. NewsMetaClass __new__')

    def __new__(cls, name, bases, attrs, *arg):
        mapping = {}
        for k, v in attrs.items():
            if(isinstance(v, Field)):
                mapping[k] = v
        # for k, v in mapping.items():
        #     del attrs[k]

        # attrs['save']=lambda self:self.

        # for k, v in mapping.items():
        #     fields.append(k)
        #     params.append('?')
            # args.append(getattr)
        attrs['__mapping__'] = mapping
        # attrs['comments'] = CharField(max_length=1000)
        clsobj = super().__new__(cls, name, bases, attrs)
        return clsobj


class News(Model, metaclass=NewsMetaClass):
    """docstring for News"""
    title = CharField(max_length=100)
    content = CharField(max_length=500)
    publish_date = DateField(default="now")
    read_count = IntField(default=0)


# news = News()
# print(dir(news))
# news.title
# AttributeError: 'News' object has no attribute 'title'

# print(news.__mapping__)
print(News.__mapping__['title'])
