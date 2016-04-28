
def RandomList(count=10):
    '''
    生成随即数组
    '''
    import random
    r = random.sample(range(count * 10), count)
    # random.shuffle(r) #洗牌
    # print(random.randint(1, 20))
    # print(random.randrange(1, 20))
    # print(random.sample(range(100), 10))
    # print(r)
    return r

# RandomList(10)


def BubbleSort(arr):
    '''
    冒泡排序
    '''
    print(arr)
    for x in range(0, len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                tmp = arr[x]
                arr[x] = arr[y]
                arr[y] = tmp
    print(arr)
    return arr

# r = RandomList()
# BubbleSort(r)


def SelectionSort(arr):
    '''
    选择排序
    '''
    print(arr)
    for x in range(0, len(arr)):
        index = x
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                index = y
        if index != x:
            tmp = arr[x]
            arr[x] = arr[index]
            arr[index] = tmp
    print(arr)
    return arr

# r = RandomList()
# SelectionSort(r)


def QuickSort(arr):
    '''
    快速排序，二分排序
    '''
    print(arr)
    for x in range(0, len(arr)):
        index = x
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                index = y
        if index != x:
            tmp = arr[x]
            arr[x] = arr[index]
            arr[index] = tmp
    print(arr)
    return arr

# r = RandomList()
# QuickSort(r)


def HuiWen(num):
    '''
    5位数回文检查
    12321
    '''
    if num // 10000 == num % 10 and num // 1000 % 10 == num % 100 // 10:
        print('huiwen:', num)
    else:
        print(num // 10000, num % 10, num // 1000 % 10, num % 100 // 10)

# HuiWen(12321)


def NumInfo(num):
    '''
    数字的位数和逆序输出
    '''
    l = [x for x in str(num)]
    l.reverse()
    for t in l:
        print(t)

# NumInfo(123)


def factorial(num):
    '''
    递归计算阶乘
    '''
    if num <= 2:
        return num
    else:
        return num * factorial(num - 1)

# r=factorial(5)
# print(r)
# # 120


def JieChengHe(num):
    import math
    '''
    计算阶乘
    math.factorial
    Return x factorial. Raises ValueError if x is not integral or is negative

    1+2!+3！=1 + 1*2 + 1*2*3
    '''
    r = 0
    for x in range(1, num + 1):
        r += math.factorial(x)

    print(r)
    return r

# JieChengHe(4)


def PrintRhombus(level):
    '''
    打印菱形
    '''
    for x in range(1, level * 2 + 1, 2):
        print((''.rjust(x, '*')).center(level * 2))
    for x in range(level * 2 - 1, 0, -2):
        print((''.rjust(x, '*')).center(level * 2))

# PrintRhombus(6)


def pingpong():
    '''
    a not x
    c not x and z
    TODO 怎么模拟
    '''
    A = ['a', 'b', 'c']
    B = ['x', 'y', 'z']


def MonkeyandPeach():
    '''
    n个桃子，一天吃一半多一个，10天后只剩一个
    '''
    r = 1
    for x in range(9, 0, -1):
        r = (r + 1) * 2
        print(x, r)
    print(r)

# MonkeyandPeach()


def wanshu(self):
    '''
    TODO
    一个数的因子之和等于其自身就是完数
    找出1000以内的完数
    '''
    pass


def replicate_cal(a, n):
    '''
    计算s=a+aa+aaa+aaaa
    n表示几个数相加
    '''
    r = 1
    for x in range(1, n + 1):
        r = r + int(''.rjust(x, str(a)))
    print(r)

# replicate_cal(5, 6)


def countchar(mystr):
    '''
    TODO
    统计字母数字和空格的个数
    '''

    pass


def ScoreGrade(score):
    '''
    条件运算符
    >90     A
    60-89   B
    <60     C
    '''
    r = 'A' if score >= 90 else ('B' if score >= 60 and score < 89 else 'C')
    print(r)
    return r
# ScoreGrade(100)


def PrimeFactors(number, result=[]):
    '''
    质因数分解
    '''
    import math
    f = math.ceil(math.sqrt(number))
    r = str(number) + '='
    w = 1
    while w:
        for x in range(2, f + 1):
            if number % x == 0:
                result.append(str(x))
                number = number / x
                f = math.ceil(math.sqrt(number))
                break
            if x == f:
                w = 0
                result.append(str(int(number)))
                break
    # str.join 必须是字符串数组
    print(r + '*'.join(result))
    return result

# PrimeFactors(163)


def ShuiXianNumber():
    '''
    水仙数，一个三位数，它的各位的立方和等于该数本身
    '''
    result = []
    for x in range(100, 999):
        if (x // 100)**3 + (x % 100 // 10)**3 + (x % 10)**3 == x:
            result.append(x)
    print(result)
    return result

# ShuiXianNumber()
# [153, 370, 371, 407]


def PrimeNumber(start, end):
    '''
    计算给定的两个数之间的素数
    '''
    import math
    pn = []
    for x in range(start, end + 1):
        s = math.ceil(math.sqrt(x))
        c = 0
        for m in range(2, s):
            if x % m == 0:
                break
            else:
                c = c + 1
        if c == s - 2:
            pn.append(x)
    print(len(pn))
    print(pn)
    return pn, len(pn)

# PrimeNumber(101, 200)
# 23
# [101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 149, 151, 157, 163, 167, 169, 173, 179, 181, 191, 193, 197, 199]


def Rabits(month, rabits=1):
    '''
    一对兔子每三个月生一对小兔子，计算每个月的兔子数量
    递归版
    '''
    if month < 3:
        return rabits
    else:
        return Rabits(month - 3, rabits * 2)

# print(Rabits(9))


def Rabits2(month):
    '''
    一对兔子每三个月生一对小兔子，计算每个月的兔子数量
    问题分析，没过三个月兔子就翻倍
    '''
    rabits = 1
    for x in range(3, month + 1, 3):
        rabits = rabits * 2
    return rabits

# print(Rabits2(9))


def CalculateMath():
    import math
    '''
    3 一个整数加上100后是一个完全平方数
    再加上168后又是一个完全平方数
    这个数字是多少
    '''
    x = 4000000
    while True:
        if type(math.sqrt(x + 100)) == int:
            if type(math.sqrt(x + 100 + 168)) == int:
                print('this number is %d' % (x))
                break
            else:
                x += 1
                continue
        else:
            x += 1
            continue
    print(x)

# CalculateMath()


def MaxofThree(x, y, z):
    '''
    5 3个数中的最大值
    print 的占位输出
    '''
    v = max(x, max(y, z))
    print('the max one of %d, %d and %d is %d' % (x, y, z, v))
    return v

# MaxofThree(12, 56, 97)
# MaxofThree(102, 56, 97)


def getUUID():
    '''
    获取UUID
    '''
    import uuid
    uid = uuid.uuid4()
    print(uid)
    print(uid.hex)
    print(str(uid).replace('-', ''))
    # 47c4ba6d-66d5-40c6-9c5f-0a1f23deb05b
    # 47c4ba6d66d540c69c5f0a1f23deb05b
    # 47c4ba6d66d540c69c5f0a1f23deb05b
# getUUID()


def getNetAmount(amount):
    '''# 企业利润'''
    import math
    alg = [x for x in range(1, 15)]
    alg[1] = lambda x: x * 0.1
    alg[2] = alg[3] = lambda x: x * 0.075
    alg[3] = alg[4] = lambda x: x * 0.05
    alg[5] = alg[6] = lambda x: x * 0.03
    alg[7] = alg[8] = alg[9] = alg[10] = lambda x: x * 0.015
    alg[11] = lambda x: x * 0.01

    r = 0
    for x in range(10, amount + 10, 10):
        v = 10 if amount - x >= 0 else amount - x + 10
        if x >= 11:
            r += alg[11](v)
        else:
            r += alg[int(x / 10)](amount)
        print(x, v, r)
    else:
        r += alg[1](amount)

    print(amount, '--', r)

# getNetAmount(6)
# getNetAmount(160)


def MultipleList():
    '''
    # 题目 - 8
    # 输出9*9口诀表
    '''
    X = range(1, 10)
    Y = range(1, 10)
    C = [[str(x) + '*' + str(y) + '=' + str(x * y) for y in Y if x >= y] for x in X]
    for r in C:
        print(r)

# MultipleList()


def PrintAC():
    '''
    # 6
    # * 输出C的图案
    '''
    print('**'.center(50))
    print('***  ***'.center(50))
    print('***    ***'.center(50))
    print('************'.center(50))
    print('**************'.center(50))
    print('***          ***'.center(50))
    print('***            ***'.center(50))
    print('***              ***'.center(50))

    print('**********'.center(50))
    print('***          ***'.center(50))
    print('***              ***'.center(50))
    print('****              ***'.center(50))
    print('****                 '.center(50))
    print('****              ***'.center(50))
    print('***              ***'.center(50))
    print('***          ***'.center(50))
    print('**********'.center(50))

# PrintAC()
