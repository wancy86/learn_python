
from attendence.models import Employee
from attendence.models import EmployeeIP

# 获取一个字段
ipList = EmployeeIP.objects.values("IP").first()
print(type(ipList))

ipList = EmployeeIP.objects.values("IP").all()
print(type(ipList))

# <class 'dict'>
print(ipList)
# {'IP': '192.168.1.41'}

# 获取多个字段
empList = Employee.objects.values("first_name", "last_name", "email")[0:2]
print(type(empList))
# <class 'django.db.models.query.QuerySet'>
print(empList)
# [
# 	{'last_name': 'Wei', 'first_name': 'Vena', 'email': 'Vena@test.com'},
# 	{'last_name': 'Wan', 'first_name': 'Mark', 'email': 'mwan@test.com'}
# ]

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
