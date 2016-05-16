from attendence.models import *
import types

'''
For test the Employee
print the attributes
'''

emp = Employee.objects.first()

for x in dir(emp):
    if(type(x) == str and x.startswith('_') == False):
        if(hasattr(emp, x) and type(emp.__getattribute__(x)) != types.MethodType):
            print(x)

# compile(filename="D\:\\GitHub\\learn_python\\temp.py",source="D:\\GitHub\\learn_python\\temp.py",mode="exec")
# execfile("D:\GitHub\learn_python\temp.py")
# D:\GitHub\learn_python\temp.py


dir(Employee)
