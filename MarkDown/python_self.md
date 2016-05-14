# Python为什么不隐式实现self

Python中类的方法都需要显式的传入一个self占位参数，这让写过C#,Java,PHP,Javascript的我很是不习惯，但是Python这么吊，肯定是有他的道理的。于是我做以下的假设来看看Python这么设计是为了解决什么问题：

就拿这个说事儿吧
```python
class News(object):
    """docstring for News"""

    def __init__(self, content,**arg):
        super(News, self).__init__()
        self.contnet=content
        self.arg = arg

    def print_conent(self):
        print('News Detail:',self.content) 
```

###假设不需要显示传入self，而是隐式的实现它，我们可以干哈呢？

1. 这个好像没什么问题
    ```python
    news =News()
    news.print_conent()
    ```
2. 但是这个会打出什么鬼呢，俺的对象呢？
    ```python
    News.print_conent()
    ```

Python是个动态语言，而且没有访问限制符这说法，你想要啥都能拿到，为了有Python可以玩儿，而且不至于被你玩儿坏，总是要牺牲点什么的。

####还有一个原因，引用Python作者Tim Peters的设计原则的第二条:
快去翻译一下，印象深刻, :)
>The Zen of Python, by Tim Peters
 >
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Note:如下的命令可以显示上面的信息
```shell
>python
>import this
```