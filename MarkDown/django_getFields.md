#django获取指定列的数据


model一般都是有多个属性的，但是很多时候我们又只需要查询特定的某一个，这个时候可以用到`values`和`values_list`

>[values()](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#values)
>>values()¶
>>
>>values(*fields)¶
>>Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.
>>
>>Each of those dictionaries represents an object, with the keys corresponding to the attribute names of model objects.

<br>

>[values_list()](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#values-list)
>>values_list()¶
>>
>>values_list(*fields, flat=False)¶
>>This is similar to values() except that instead of returning dictionaries, it returns tuples when iterated over. Each tuple contains the value from the respective field passed into the values_list() call — so the first item is the first field, etc.



看下面的代码：

###利用values查询
```python
from attendence.models import Employee
from attendence.models import EmployeeIP

#获取一个字段
ipList = EmployeeIP.objects.values("IP").first()
print(type(ipList))
# <class 'dict'>
print(ipList)
# {'IP': '192.168.1.41'}

#获取多个字段
empList = Employee.objects.values("first_name", "last_name", "email")[0:2]
print(type(empList))
# <class 'django.db.models.query.QuerySet'>
print(empList)
# [
#   {'last_name': 'Wei', 'first_name': 'Vena', 'email': 'Vena@test.com'},
#   {'last_name': 'Wan', 'first_name': 'Mark', 'email': 'mwan@test.com'}
# ]
```

###利用values_list查询
```python
ipList = EmployeeIP.objects.values_list("IP").first()
print(type(ipList))
# <class 'tuple'>
print(ipList)
# ('192.168.1.111',)

ipList = EmployeeIP.objects.values_list("IP")[0:2]
print(type(ipList))
# <class 'django.db.models.query.QuerySet'>
print(ipList)
# [('192.168.1.41',), ('192.168.1.44',)]
print(type(ipList[0]))
# <class 'tuple' >
print(ipList[0])
# 192.168.1.111
```

###values和values_list的差别
从上面的代码中我们可以看到返回结果类型上细微的差别
* vlaues - 
    * 单条记录 - `<class 'dict'>`
    * 多条记录 - `<class 'django.db.models.query.QuerySet'>`
* vlaues_list - 
    * 单条记录 - `<class 'tuple'>`
    * 多条记录 - `<class 'django.db.models.query.QuerySet'>`
