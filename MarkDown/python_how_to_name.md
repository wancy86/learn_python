#Python下划线与命名规范

####先看结论，节省只想知道答案你的宝贵时间![](http://mat1.gtimg.com/www/mb/images/face/21.gif)：

1. \_xxx     不能用于`from module import *` 以单下划线开头的表示的是`protected`类型的变量。即保护类型只能允许其本身与子类进行访问。

2. \_\_xxx    双下划线的表示的是`private`类型的变量。只能是允许这个类本身进行访问了。

3. \_\_xxx\_\_  定义的是特列方法。像\_\_init\_\_之类的

###详解

以下分四种情况说明下划线的作用，python对成员域没有严格控制，大部份只是作为命名规范存在，以下英文部份摘自python官方网站

>_single_leading_underscore: weak "internal use" indicator.  E.g. "from M import *" does not import objects whose name starts with an underscore.

\_单下划线开头：弱`内部使用`标识，如：`from M import *`，将不导入所有以下划线开头的对象，包括包、模块、成员

 >single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.Tkinter.Toplevel(master, class_='ClassName')

单下划线结尾\_：只是为了避免与python关键字的命名冲突


>__double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

\_\_双下划线开头：模块内的成员，表示私有成员，外部无法直接调用


>__double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces.  E.g. __init__,__import__ or __file__.  Never invent such names; only use them as documented.

\_\_双下划线开头双下划线结尾\_\_：指那些包含在用户无法控制的命名空间中的`魔术`对象或属性，如类成员的\_\_name\_\_ 、\_\_doc\_\_、\_\_init\_\_、\_\_import\_\_、\_\_file\_\_、等。推荐永远不要将这样的命名方式应用于自己的变量或函数。

另外，以上说的大部分都是与模块成员相关的，包和模块的命名规范又有哪些需要注意的呢？

>Package and Module Names                
Modules should have short, all-lowercase names.  Underscores can be used in the module name if it improves readability.  Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.     
Since module names are mapped to file names, and some file systems are case insensitive and truncate long names, it is important that module names be chosen to be fairly short -- this won't be a problem on Unix,but it may be a problem when the code is transported to older Mac or Windows versions, or DOS.

包和模块：模块应该使用尽可能短的、全小写命名，可以在模块命名时使用下划线以增强可读性。同样包的命名也应该是这样的，虽然其并不鼓励下划线。

以上这些主要是考虑模块名是与文件夹相对应的，因此需要考虑文件系统的一些命名规则的，比如Unix系统对大小写敏感，而过长的文件名会影响其在Windows\Mac\Dos等系统中的正常使用。

>Class Names
Almost without exception, class names use the CapWords convention.Classes for internal use have a leading underscore in addition.

类：几乎毫无例外的，类名都使用首字母大写开头(Pascal命名风格)的规范。使用\_单下划线开头的类名为内部使用，上面说的from M import *默认不被告导入的情况。

>Exception Names

>Because exceptions should be classes, the class naming convention applies here.  However, you should use the suffix "Error" on your exception names (if the exception actually is an error).


异常：因为异常也是一个类，所以遵守类的命名规则。此外，如果异常实际上指代一个错误的话，应该使用`Error`做后缀

>Global Variable Names

>(Let's hope that these variables are meant for use inside one module only.)  The conventions are about the same as those for functions.Modules that are designed for use via "from M import *" should use the __all__ mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").


>Function Names
>Function names should be lowercase, with words separated by underscores as necessary to improve readability. mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

函数：小写、下划线分词，如def has\_key(ch):

>Function and method arguments

>Always use 'self' for the first argument to instance methods.Always use 'cls' for the first argument to class methods.If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption.  Thus "print_" is better than "prnt".  (Perhaps better is to avoid such clashes by using a synonym.)


>Method Names and Instance Variables
>Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability. Use one leading underscore only for non-public methods and instance variables.
>To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

>Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a.  (An insistent
>user could still gain access by calling Foo._Foo__a.)  Generally, double
>leading underscores should be used only to avoid name conflicts with
>attributes in classes designed to be subclassed.
>Note: there is some controversy about the use of __names (see below).
 

>Constants
>Constants are usually defined on a module level and written in all capital letters with underscores separating words.  Examples include MAX_OVERFLOW and TOTAL.
 

构造函数及其他：

```python
class a():

     def __init__(self):

              self._hour = 0

              self._minute = 0
```

\_\_init\_\_为类的构造函数，每次创建类对象时，都会执行构造函数。构造函数（\_\_init\_\_）会初始化类对象属性，并且返回None。python类还可以定义其他的特殊方法，这些方法之前、之后都会有双下划线（\_\_）。

构造函数用单一的前置下划线（\_）来创建属性。属性名以单下划线开头。虽然在python语法中没有特殊的含义，但单下划线是python程序员使用类是约定的使用的符号，表明程序员不希望类的用户直接访问属性。如果程序要求访问属性，程序员会提供其他途径。

私有属性：

python中，对象的属性是肯定能被访问的——没有办法阻止其他代码访问属性。但python也提供了特殊的机制来防止任意的访问数据。

这种特殊机制叫做`名称重整`，使用方法则为：为属性名附加双下划线前缀（\_\_）。来个例子？：

在类A的构造函数（\_\_init\_\_）中这样写到：
```python
class A():

       def __init__(self):

             self.__hour = 0

B=A( )
```

现在，如果你想采取常用的方法`print B.\_\_hour`，那么你将得到的反馈信息不是理想的`0`，而是一则异常。我们换个方式来试试：`print B.\_A\_\_hour`

如你所愿了吗？

当构造函数的属性名附加双下划线前缀（\_\_）后，python就会创建`\_类名\_\_属性名`这样的属性，而不是名为`\_\_属性名`的属性。

值得说明的是，经过`名称重整`后的属性依然是可以通过`对象.\_类名\_\_属性名`的方法访问、甚至修改（如执行`B.\_A\_\_hour = 5`是可以通过的），但这样的使用方式将违背作者的数据封装意图。

Python 用下划线作为变量前缀和后缀指定特殊变量。

\_xxx      不能用'from module import *'导入 
\_\_xxx\_\_   系统定义名字 
\_\_xxx     类中的私有变量名 

核心风格：避免用下划线作为变量名的开始。

因为下划线对解释器有特殊的意义，而且是内建标识符所使用的符号，我们建议程序员避免用下划线作为变量名的开始。一般来讲，变量名\_xxx被看作是`私有 的`，在模块或类外不可以使用。当变量是私有的时候，用\_xxx 来表示变量是很好的习惯。因为变量名\_\_xxx\_\_对Python 来说有特殊含义，对于普通的变量应当避免这种命名风格。

"单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
"双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

以单下划线开头（\_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用`from xxx import *`而导入；以双下划线开头的（\_\_foo）代表类的私有成员；以双下划线开头和结尾的（\_\_foo\_\_）代表python里特殊方法专用的标识，如 \_\_init\_\_（）代表类的构造函数。

 



 

 