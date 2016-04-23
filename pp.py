# import uuid
# print(uuid.uuid4())
# # dad958592e9d43e59b5c4dd3e6eb4707


class Pclass(object):
    """docstring for Pclass"""
    num = 10

    def __init__(self):
        super(Pclass, self).__init__()

p = Pclass()
print(p.num)    #10
p.num = p.num + 1
print(p.num)    #11
print(Pclass.num)   #10

Pclass.age=12
print(Pclass.age)   #12
print(p.age)    #12

p.xxx=555
print(p.xxx) #555
print(Pclass.xxx) #AttributeError: type object 'Pclass' has no attribute 'xxx'

