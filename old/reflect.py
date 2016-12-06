# reflect.py
# 获取对象的所有的方法和属性
# param: object
# return: object{type,functions,properties}


class TestCls(object):
    """docstring for TestCls"""
    age = [1, 2, 3]

    def __init__(self, **arg):
        super().__init__()
        self.arg = arg

    def SayHello(self, name):
        '''
        say hello to [name]
        '''
        print("hello", name)


import inspect

testcls = TestCls()
testcls.SayHello('Mark')
print('------------')
for x in inspect.getmembers(TestCls):
    print(x)


# print(inspect.getmembers(TestCls))
# Output: [('__add__', <slot wrapper '__add__' of ... ...

isinstance(a, class)
type(a)
types.FunctionType
getattr
setattr
hasattr(object, name)
len()
__len__


class News(object):
    """docstring for News"""

    def __init__(self, content, **arg):
        super(News, self).__init__()
        self.contnet = content
        self.arg = arg

    def print_conent(self):
        print('News Detail:', self.content)


news = News()
news.print_conent()

News.print_conent()
