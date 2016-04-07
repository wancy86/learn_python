

# ------------------------------------------------
print("----------------tuple-元组------------------")
t=1,2,3
print(t)

t2=1,'sss',2
print(t2)

# 变量的赋值
stock=('002582',28.10,28.80,28.90,28.00)
code,open_price,close_price,high_price,low_price=stock
print(code)

# namedtuple
# 可以自定义
from collections import namedtuple
Stock=namedtuple('Stock','code price')
s=Stock('002852',28.5)
print(s)

print("----------------逻辑控制------------------")
# 默认转换
if 1:
    print('123')
else:
    print('true')
if not None:
    print('false')
else:
    print('true')
if not False:
    print('false')
else:
    print('true')
if not 0.00:
    print('false')
else:
    print('true')
if not []:
    print('false')
else:
    print('true')
if not "":
    print('false')
else:
    print('true')

# 
date="2000-02-06"
year, month, day=tuple(date.split('-'))
print(year)
# 添加处理方法，直接int转换
year1, month1, day1=tuple([int(item) for item in date.split('-')])
year2, month2, day2=tuple(int(item) for item in date.split('-'))
year3, month3, day3=(int(item) for item in date.split('-'))

# 获取日期的最后一天
last_day=None
if month in ('01','03','05','07','08','10','12'):
    # pass #什么也不做的意思，格式占位
    last_day=31
elif  month in('04','06','09','11'):
    last_day=30 
else:
    if (int(year)%4==0 and int(year)%100!=0) or int(year)%400==0:
        last_day=29
    else:
        last_day=28

print(last_day)

print("----------------逻辑控制-For--------------")

xxx="""
    for x in range(0,101)
        print(x)"""
print(xxx)
for x in range(0,101):
    print(xxx)

print("----------------逻辑控制------------------")

        
print("----------------range VS xrange-----------")
# range(100) 返回数组
# xrange(100) 返回迭代器，不会开辟数组空间
# 循环中应该使用xrange
for x in xrange(1,10):
    print(x)

print("------------------------------------------")

