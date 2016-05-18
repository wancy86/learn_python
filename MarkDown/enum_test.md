# Python的

Python的没有我们有两种用法：
1. 创建Enum的实例
2. 创建Enum的subclass

###创建Enum的实例
```python
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 用法
print(Month.Jan.value)

for k, v in Month.__members__.items():
    print(k, v.value)

```

###创建Enum的subclass
```python

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

```

###运行结果
```python
# 1
# Jan 1
# Feb 2
# Mar 3
# Apr 4
# May 5
# Jun 6
# Jul 7
# Aug 8
# Sep 9
# Oct 10
# Nov 11
# Dec 12
# ----------------------------------------
# 0
# Jan 0
# Feb 1
# Mar 2
# Apr 3
# May 4
# Jun 5
# Jul 6
# Aug 7
# Sep 8
# Oct 9
# Nov 10
# Dec 11
```