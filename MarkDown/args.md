#Python中的参数

###1. python函数参数有多重形式：
    * test(arg1,arg2,`*args`)
    * test(arg1,arg2,`*args`,`**kwargs`)


###2. 其中比较糊弄人的是：`*args`和`**kwargs`
`*args`       变长的占位参数列表   - `<class 'tuple'>`
`**kwargs`    变长的键值对参数列表 - `<class 'dict'>`

###3. 什么是占位参数：
`test(arg1,arg2)` 参数括弧中列出的标识符就是占位参数
`*args`变长占位参数是用来发送一个非键值对的可变数量的参数列表给一个函数, 可以遍历得到它

```python
def test_var_args(f_arg, *argv):
    print(type(argv))
    # <class 'tuple'>
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```


###4. 什么是键值对参数：
`**kwargs` 允许你将变长度的键值对, 作为参数传递给一个函数, 说白了就是函数的参数是个dict,但是不能直接传个dict给函数，得加上前导`**`解包

```python
def test_kwarg(**kwargs):
    print(type(kwargs))
    # <class 'dict'>
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

test_kwarg(name="foo")
test_kwarg(name="foo", age=26)
test_kwarg(**{'name': "foo", 'age': '26'})
```

###5. 综合看一个更复杂的例子

```python
def test_kwarg(name, age, *args, **kwargs):
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
```

###6. Note: 函数调用时，`*args`, `**kwargs`是可选的，但是前面的常规参数是必须的

###7. over![](http://mat1.gtimg.com/www/mb/images/face/98.gif)