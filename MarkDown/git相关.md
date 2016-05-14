#Git使用相关

使用git这么久还是时不时碰到小问题，根本原因在于没有仔细研究和做笔记

##Git修改remote地址
之前一直使用的ssh的地址，估计是没配置好，每次都需要输密码烦死了，今天看到个用https的模式可以永久记住密码，那还不赶快拿来用，这也能省下几秒钟时间啊

```
//查看当前地址
git remote -v

//删除已有的地址，我的是ssh的，git@github.com:wancy86/BSQJ.git
git remote rm origin

//将https的地址加进来
git remote add origin https://github.com/wancy86/BSQJ.git

git remote -v
```

##Git在https模式下记住密码

``` 
git config --global credential.helper store
```

##https和ssh有什么差别

这两种方式的主要区别在于：
使用https url克隆对初学者来说会比较方便，复制https url然后到git Bash里面直接用clone命令克隆到本地就好了，但是每次fetch和push代码都需要输入账号和密码，这也是https方式的麻烦之处。

而使用SSH url克隆却需要在克隆之前先配置和添加好SSH key，因此，如果你想要使用SSH url克隆的话，你必须是这个项目的拥有者。否则你是无法添加SSH key的，另外ssh默认是每次fetch和push代码都不需要输入账号和密码，如果你想要每次都输入账号密码才能进行fetch和push也可以另外进行设置
<br><br>
