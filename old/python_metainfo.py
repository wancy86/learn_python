# Python获取对象的元数据
class Dog(object):
    """docstring for Dog"""
    animal = 1
    ispet = 1

    def __init__(self, name):
        super(Dog, self).__init__()
        self.name = name

    def bark(self):
        print('dog', self.name, 'is barking...w.w.w...')


# 获取元数据信息
# 获取类的属性类表
print(dir(Dog))

# 公用
# __doc__: 文档字符串。如果模块没有文档，这个值是None。
# __name__: 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。

# module
# __dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。
# __file__: 包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！

# class
# __module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。
# __bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。

# instance
# __class__: 该实例的类对象。对于类Cat，cat.__class__ == Cat 为 True。

# method
# __self__: 仅方法可用，如果是绑定的(bound)，则指向调用该方法的类（如果是类方法）或实例（如果是实例方法），否则为None。

# funtion
# __dict__: 函数的可用属性；另外也可以用属性名func_dict。不要忘了函数也是对象，可以使用函数.属性名访问属性（赋值时如果属性不存在将新增一个），或使用内置函数has/get/setattr()访问。不过，在函数中保存属性的意义并不大。
# func_defaults: 这个属性保存了函数的参数默认值元组；因为默认值总是靠后的参数才有，所以不使用字典的形式也是可以与参数对应上的。
# func_code: 这个属性指向一个该函数对应的code对象，code对象中定义了其他的一些特殊属性，将在下文中另外介绍。
# func_globals: 这个属性指向当前的全局命名空间而不是定义函数时的全局命名空间，用处不大，并且是只读的。
# func_closure: 这个属性仅当函数是一个闭包时有效，指向一个保存了所引用到的外部函数的变量cell的元组，如果该函数不是一个内部函数，则始终为None。这个属性也是只读的。

import inspect
print(Dog.__name__)
print(Dog.__dict__)

dog = Dog('keke')
im = dog.bark
print(dir(im))

print(inspect.ismethod(im))
print(inspect.isfunction(im))
print(inspect.isroutine(im))
print(inspect.getmembers(im))
