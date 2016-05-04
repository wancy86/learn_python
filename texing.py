
# map()、zip()、filter()、reduce()

# 1. map
fruit = (('apple', 'banana'), ('red', 'blue'), ('a',), ('b',))
i = 0


def mapfunc(x):
    return 'i love ' + x[0]

for i in map(mapfunc, fruit):
    print(i)

# i love apple
# i love red
# i love a
# i love b
# [Finished in 0.1s]

print('-----------------------map')
# 2. 两个数组之间对应操作
a = [1, 2, 3, 4]
b = [4, 3, 2, 1]


def mapfunc2(x, y):
    return x + y
for z in map(mapfunc2, a, b):
    print(z)
# lambda
for z in map(lambda x, y: x + y, a, b):
    print(z)

# 5
# 5
# 5
# 5

list2 = [1, 2, 3, 4]
for a in map(lambda x: x**2, list2):
    print(a)
for x in list2:
    print(x)

print('-----------------------filter')
for b in filter(lambda x: x <= 3, list2):
    print(b)

print('-----------------------zip')
# index对应组合成tuple的list
list3 = [1, 2, 3, 4]
list4 = [11, 22, 33, 44]
z = zip(list3, list4)
for x in z:
    print(x)
print('---unzip')
# TODO 到底怎么用的？
print(zip(*zip(list3, list4)))


print('-----------------------reduce')
# 每次取两个值进行操作，最终返回一个值
# 必须是二元函数
from functools import reduce
a = reduce(lambda x, y: x * y, [1, 2, 3])
print(a)
b = reduce(lambda x, y: x * y, [1, 2, 3], 10)
print(b)
