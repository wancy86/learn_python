'''
永远为正数的int类型
'''


class PositiveInteger(int):

    def __init__(self, value):
        super().__init__(self, abs(value))

# i = PositiveInteger(-3)
# print(i)
# # TypeError: object.__init__() takes no parameters


class PositiveInteger(int):

    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))
i = PositiveInteger(-3)
print(i)
