# 1.找到重复的元素
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
# 输出: ['b', 'n']

# 2.找到重复的元素
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
# 输出: set(['b', 'n'])

# 过滤掉重复的元素
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set(iter(some_list))
print(duplicates)
# 输出： {'c', 'n', 'a', 'm', 'd', 'b'}
print([x for x in some_list if some_list.count(x) > 1])

# 差集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
# 输出: set(['red'])

# 差集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# 输出: set(['brown'])

# 你也可以用符号来创建集合，如：
a_set = {'red', 'blue', 'green'}
print(type(a_set))
# 输出: <type 'set'>

# 下面的会变成字典
a_set = {'red': '123'}
print(type(a_set))
# 输出: <class 'dict'>


# 三元运算符
is_fat = False
state = "fat" if is_fat else "not fat"
print(state)

state = 1 if is_fat else 0
print(state)

# 利用元素和数组实现
# 有风险慎用
state = (0, 1)[True]
print(state)

state = ['0-index','1-index'][True]
print(state)
# 这之所以能正常工作，是因为在Python中，True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据。


