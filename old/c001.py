
class Point(object):
    """docstring for Point"""
    def __init__(self,x=0,y=0, *arg):
        super(Point, self).__init__()
        self.arg = arg
        self.x=x
        self.y=y
        self.c=1000

    def calc_distence(self):
        import math
        # 鏂规牴
        result= math.sqrt(self.x**2+self.y**2)
        return result

    @property
    def num(self):
        return self.c


        

# 
p=Point(3,4)
result=p.calc_distence()
print("the distence is",result)

print(Point.num)
print(p.num)


print('\r--------------------@property')
class ProTest(object):
    """docstring for ProTest"""
    _num=1000
    def __init__(self, *arg):
        super(ProTest, self).__init__()
        self.arg = arg

    @property
    def num(self):
        return self._num
    @num.setter
    def num(self, value):
        self._num = value

pt=ProTest()
print(ProTest.num)      #<property object at 0x021B1A20>
print(pt.num)           #1000
pt.num=120
print(pt._num)          #120
print(pt.num)           #120


print('\r--------------------static method')
class StaticTest(object):
    """docstring for StaticTest"""
    def __init__(self, *arg):
        super(StaticTest, self).__init__()
        self.arg = arg

print('\r--------------------class method')
class KlassTest(object):
    """docstring for KlassTest"""
    def __init__(self, *arg):
        super(KlassTest, self).__init__()
        self.arg = arg

print('\r--------------------class test')
class ourDate(object):
    day =0
    month =0
    year =0

    def __init__(self,day=0,month=0,year=0):
        self.day=day
        self.month=month
        self.year=year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date1 = cls(day, month, year)
        print('>from_string on:',cls)
        return date1

    @staticmethod
    def is_date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        try:
            assert 0<= day <=31
            assert 0<= month <=12
            assert 0<= year <=3999
        except AssertionError:
            return False
        return  True

    def __str__(self):
        return str(self.day)+'-'+str(self.month)+'-'+str(self.year)

date2 =ourDate.from_string('11-09-2012')
print(date2)
check = ourDate.is_date_valid(str(date2))
print('date2 is valied:',check)

class MyDate(ourDate):
    """docstring for MyDate"""
    pass

mydate=MyDate(13,4,2016)
print(mydate)
print('mydate is valid:',MyDate.is_date_valid(str(mydate)))
mydate2=MyDate.from_string('14-04-2016')
print(mydate2)


# >from_string on: <class '__main__.ourDate'>
# 11-9-2012
# date2 is valied: True
# 13-4-2016
# mydate is valid: True
# >from_string on: <class '__main__.MyDate'>
# 14-4-2016