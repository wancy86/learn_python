# mmath.py

def fn_a(x,y):
    return x+y

print(fn_a(1,2))


# 可变参数
def fn_b(*args):
    return sum(args)

print(fn_b(1,2,3,4,8))

# 混合
def fn_c(x,y,*args):
    return x+y+sum(args)
    pass

print(fn_c(1,2,3,4,5))

# 默认值参数
def fn_d(x,y,z=100):
    return x+y+z

print(fn_d(1,2))

def fn_e(x,y,z=100,*args):
    return x+y+z+sum(args)

print(fn_e(1,2,3,20))
print(fn_e(1,2,3,20,30,40))
# print(fn_e(1,2,20,z=3))

print('\n')
def list_employees(company,*args):
    welcome=company+' welcome you: '
    for x in args:
        welcome+=', '+x

    print(welcome)

list_employees('Max','mark')
list_employees('Max','mark','Miles')


# 字典参数
def fn_f(name,age):
    print(name+' is '+age + ' years old.')

person={'name':'Mark','age':'29'}
fn_f(**person)

