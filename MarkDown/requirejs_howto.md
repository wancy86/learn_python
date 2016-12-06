#requirejs的使用
-----------------

####加载网络模块
-----------------

[使用CDN ](https://github.com/requirejs/example-jquery-cdn)

```javascript
requirejs.config({
    "baseUrl": "js/lib",
    "paths": {
      "app": "../app",
      "jquery": "//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min"
    }
});
```

####shim配置
https://github.com/requirejs/example-jquery-shim

```javascript
requirejs.config({
    "baseUrl": "js/lib",
    "paths": {
      "app": "../app"
    },
    "shim": {
        "jquery.alpha": ["jquery"],
        "jquery.beta": ["jquery"]
    }
});
```

// Load the main app module to start the app
requirejs(["app/main"]);
App/main.js is where the app logic is:

```javascript
define(["jquery", "jquery.alpha", "jquery.beta"], function($) {
    //the jquery.alpha.js and jquery.beta.js plugins have been loaded.
    $(function() {
        $('body').alpha().beta();
    });
});
``

####加载非AMD规范模块
-----------------
定义依赖和导出对象

```javascript
　　require.config({
　　　　shim: {

　　　　　　'underscore':{
　　　　　　　　exports: '_'
　　　　　　},
　　　　　　'backbone': {
　　　　　　　　deps: ['underscore', 'jquery'],
　　　　　　　　exports: 'Backbone'
　　　　　　}
　　　　}
　　});
```


####requirejs插件
-----------------
http://www.ruanyifeng.com/blog/2012/11/require_js.html

domready插件，可以让回调函数在页面DOM结构加载完成后再运行。
```
　require(['domready!'], function (doc){
　　　　// called once the DOM is ready
　　});
```

text和image插件，则是允许require.js加载文本和图片文件。
```
define([
　　　　'text!review.txt',
　　　　'image!cat.jpg'
　　　　],

　　　　function(review,cat){
　　　　　　console.log(review);
　　　　　　document.body.appendChild(cat);
　　　　}
　　);
```

类似的插件还有json和mdown，用于加载json文件和markdown文件。
