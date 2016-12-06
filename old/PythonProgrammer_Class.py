'''metaclass是类的模板，所以必须从`type`类型派生：'''


class ProgrammerMetaClass(type):
    """docstring for Programmer"""
    def __new__(cls, name, bases, attrs):
        # 这里可以对类胡作非为的修改
        # 1.添加play_cool method
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
print(PythonProgrammer.has_girlfriend)
# print(pp.has_girlfriend)
