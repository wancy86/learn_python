print('\n---------------------------------')
# 类的方法
class Point():
    """docstring for Point"""

    def __init__(self, x=0, y=0):
        super(Point, self).__init__()
        self.x = x
        self.y = y

    # 这个方法没有给定self参数，实例对象不能访问，但是实例化的时候会开辟内存
    def display():
        print('just display message for class...')


p1 = Point(2, 8)
Point.display()
# p1.display()

print('\n---------------------------------')

import math
class Point():
    """docstring for Point"""

    def __init__(self, x=0, y=0):
        super(Point, self).__init__()
        self.x = x
        self.y = y

    def calculate_distance(self):
        
        result = math.sqrt(self.x**2 - self.y**2)
        print('this distance is', result)
        return result
    
    # 私有方法， 自动添加了 _ClassName前缀
    def __sayHello():
        print('hello class function...')

Point._Point__sayHello()
p1 = Point(2, 8)
# p1.calculate_distance()
# Point.calculate_distance(self=p1)

print('\n---------------------------------')


class Human(object):
    """docstring for Human"""

    def __init__(self, *arg):
        super(Human, self).__init__(*arg)
        self.arg = arg
    # 类的方法一定要有个self参数

    def hello(self, msg):
        print('Hello....', msg)

human = Human()
human.name = 'Tom'
print(human.name)
human.hello(human.name)
