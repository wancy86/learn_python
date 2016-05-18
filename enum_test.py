
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 用法
print(Month.Jan.value)

for k, v in Month.__members__.items():
    print(k, v.value)


print('----------------------------------------')


from enum import Enum, unique


@unique
class Month2(Enum):
    Jan = 0
    Feb = 1
    Mar = 2
    Apr = 3
    May = 4
    Jun = 5
    Jul = 6
    Aug = 7
    Sep = 8
    Oct = 9
    Nov = 10
    Dec = 11

# 用法
print(Month2.Jan.value)

for k, v in Month2.__members__.items():
    print(k, v.value)
