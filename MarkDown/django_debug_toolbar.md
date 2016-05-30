#安装和使用的django的debug_toolbar


####Django Debug Toolbar安装

1. 安装Django Debug Toolbar
`pip install django-debug-toolbar`

2. 将debug_toolbar复制到项目根目录下，打开项目settings.py，首先确保
`DEBUG = True`

3. 找到INSTALLED_APPS，添加：`'debug_toolbar',`, 找到MIDDLEWARE_CLASSES，添加：`'debug_toolbar.middleware.DebugToolbarMiddleware',`

4. 在settings.py末尾添加设置项INTERNAL_IPS，用以设置允许访问debug_toolbar的IP地址`INTERNAL_IPS = ('127.0.0.1',)`


####报错及解决

运行后发现报错：
`'module' object has no attribute 'getrusage'`
这个是它的timer出问题了，直接注释掉
```python
PANELS_DEFAULTS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    # #Throwing AttributeError: 'module' object has no attribute 'getrusage'
    #'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
```
再运行还是不行，看文件加载得知jquery.min.js没有被加载成功。这就是问题所在。
去debug_toolbar的settings里面一看：
`'JQUERY_URL': '//ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js',`
我大天朝必然是不行的吗, 如果项目中有jquery直接注释掉这行，否则就改成其他的可用的地址
`DEBUG_TOOLBAR_CONFIG = {  'JQUERY_URL' : r"http://code.jquery.com/jquery-2.1.1.min.js"}`


####然而并没有什么卵用啊
![]()





