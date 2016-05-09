MarkDown
--------

#标题

\#h1

\#\#h2

\#\#\#h3

#h1
##h2
###h3

#代码段
代码段缩进4个空格即可，如下：


    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-4">
          <div class="checkbox">
            <label>
              <input type="checkbox" id="autologin" name="autologin" value="1"> 30天自动登录
            </label>
          </div>
        </div>
    </div>   


#链接
\[博客园\]\(http://www.cnblogs.com/cmt\)

[博客园](http://www.cnblogs.com/cmt)

#图片
\!\[博客园\]\(http://www.cnblogs.com/images/logo_small.gif\)

![博客园](http://www.cnblogs.com/images/logo_small.gif)

#无序列表
这个比较随意，\+ \- \* 都可以表示无序列表，**不要忘了后面要加一个空格**

+ aaaaaaa
- bbbbbbb
* ccccccc

#有序列表
只要使用数字后跟一个 \. 开头就可以了, 不用在意编号，MarkDown会自动编号
使用四个空格可以实现嵌套的列表

2. aaaaaaa
    2. aaa
    2. bbb
        3. 111
2. bbbbbbb
2. ccccccc

#pre-formatted
有三种方式：
1. 使用三个单引号
    \`\`\`language 
    你的代码
    \`\`\`
2. 使用四个空格缩进就能识别为代码段了

```html
<div id="pagerdiv">
    <table class="table table-bordered table-hover table-striped">
        <tr>
            <th width="20%">Name</th>
            <th width="20%">IP</th>
            <th width="20%">Action</th>
        </tr>
    </table>
    <div id="pagerbar" style="margin-top:-20px;"></div>
</div>
```

```python
class TestCls(object):
    """docstring for TestCls"""
    age = 29

    def __init__(self, **arg):
        super().__init__()
        self.arg = arg

    def SayHello(self, name):
        '''
        say hello to [name]
        '''
        print("hello", name)
```

#文字特殊处理
```
*MarkDown*         #斜体
_MarkDown_         #斜体
**MarkDown**       #加粗
__MarkDown__       #加粗
```

#转义
元字符和正则式一样使用\来转义
```
\\ \` \* \_ \{ \} \[ \] \( \) \# \+ \- \. \!
```
html效果：
\\ \` \* \_ \{ \} \[ \] \( \) \# \+ \- \. \!