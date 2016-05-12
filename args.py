
def test_kwarg(name, age, *args, **kwargs):
    print('--------------------------------------')
    print('all positional args:')
    print('name:{0}'.format(name))
    print('age:{0}'.format(age))
    print('\n')

    print('all optional positional *args:')
    for arg in args:
        print('args:{0}'.format(arg))

    print('\n')
    print('all keywords **kwargs:')
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


# 只有占位参数
test_kwarg("foo", 26)
# 占位参数 + 可选占位参数
test_kwarg("foo", 26, 'opt1')
# 占位参数 + 键值对参数
test_kwarg("foo", 26, kw1=100, kw2=200)
# 占位参数 + 可选占位参数 + 键值对参数
test_kwarg("foo", 26, 'opt1', 'opt2', kw1=100, kw2=200)
