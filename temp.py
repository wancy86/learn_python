# from attendence.models import *
# import types

# emp = Employee.objects.first()

# for x in dir(emp):
#     if(type(x) == str and x.startswith('_') == False):
#         if(hasattr(emp, x) and type(emp.__getattribute__(x)) != types.MethodType):
#             print(x)

# compile(filename="D\:\\GitHub\\learn_python\\temp.py",source="D:\\GitHub\\learn_python\\temp.py",mode="exec")
# execfile("D:\GitHub\learn_python\temp.py")
# D:\GitHub\learn_python\temp.py


class TestCls():
    """docstring for TestCls"""

    def __init__(self, name):
        print('init')
        self.name = name

    def __new__(cls, name):
        print('new')
        return super().__new__(cls)


c = TestCls("CooMark")
print(type(c))
print(c.name)
