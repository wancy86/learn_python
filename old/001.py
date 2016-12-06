m=123456789
n=88888888888888888888888888888888
print("m is",m)
print("n is",n)
print("m*n is",m*n)
print("---------------------------------------")
print(10/3)
print(10//3)
print(10%3)

print("---------------------------------------")
# help(print)

print(2**3)#8

print('hello'*3)

print("----------------字符串----------------")
# 单引号转译, 前面加r则不转译
# 双引号不转译
# 
print("''")
print('""')
print('123\r\n456')
print(r'123\r\n456')
print('123''234')

print("----------------字符串----------------")
# 字符串支持字符数组，start_index, end_index
mystr='hello world'
print(mystr[0:2])
print(mystr[-3:-1])
print(len(mystr))
h='''
nihao
ma
'''
print(h)

print("----------------Class----------------")
class Person(object):
    """docstring for Person"""
    def __init__(self,):
        super(Person,self).__init__()

    def __len__(self):
        return 10
    # 多行注释
    '''    
    def __bool__(self):
        return true;
    '''

print("----------------List----------------")
L1=[1,2,3,4,5,6,7,8,9]
print(L1[2])
print(L1[1:4:2])
print(L1[0:4])
# 反向index
# help(list)
print(L1)
print(L1[::-1])
print(L1[-1:-20:-1]) 
# L1.add(11,12,13)
print(L1)


dir()