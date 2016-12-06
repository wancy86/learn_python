class TestCls():
    """docstring for TestCls"""

    def __init__(self, name):
        print('init...')
        print(self)
        print(type(self))
        self.name = name

    def __new__(cls, name):
        print('new...')
        print(cls)
        print(type(cls))
        return super().__new__(cls)


c = TestCls("CooMark")
