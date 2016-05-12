#Python的datetime

总会用到日期格式化和字符串转成日期，贴点代码以供参考，其实API真的是很全的，可是又不知道具体的method...![](http://mat1.gtimg.com/www/mb/images/face/98.gif)


`datetime.datetime.strftime(format_str)`：返回格式化后的日期字符串

`datetime.datetime.strptime(date_str,format_str)`：由字符串转为日期型


*格式化参数*

```
两个函数都涉及日期时间的格式化字符串，列举如下：
%a Abbreviated weekday name
%A Full weekday name
%b Abbreviated month name
%B Full month name
%c Date and time representation appropriate for locale
%d Day of month as decimal number(01 - 31)
%H Hour in 24 - hour format(00 - 23)
%I Hour in 12 - hour format(01 - 12)
%j Day of year as decimal number(001 - 366)
%m Month as decimal number(01 - 12)
%M Minute as decimal number(00 - 59)
%p Current locale's A.M. / P.M. indicator for 12 - hour clock
%S Second as decimal number(00 - 59)
%U Week of year as decimal number, with Sunday as first day of week(00 - 51)
%w Weekday as decimal number(0 - 6 Sunday is 0)
%W Week of year as decimal number, with Monday as first day of week(00 - 51)
%x Date representation for current locale
%X Time representation for current locale
%y Year without century, as decimal number(00 - 99)
%Y Year with century, as decimal number
%z, % Z Time - zone name or abbreviation
no characters if time zone is unknown
% % Percent sign
```

*代码示例*
```python
from datetime import datetime

d = datetime.now()
print(d)
# 2016-05-11 17:37:32.318566
print(d.strftime('%y-%m-%d'))
# 16-05-11
print(d.strftime('%Y-%m-%d'))
# 2016-05-11
print(d.strftime('%Y-%m-%d %H:%M:%S'))
# 2016-05-11 17:37:32

# 字符串转日期就是要告诉程序传入的字符串各部分代表什么
datetime.strptime('2016-05-11 17:37:32', '%Y-%m-%d %H:%M:%S')
```
