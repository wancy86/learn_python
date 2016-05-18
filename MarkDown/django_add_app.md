#django添加app

###执行命令生成基本目录结构
python manage.py startapp MyApp1

###个性优化

一个model一个`class`，一个控制器一个`class`：
删除views.py, models.py
mkdir templates/MyApp1
mkdir models
mkdir views
在views/和models/下添加 __init__.py

####Note:
如果在views/__init__.py中添加:
from .myview1 import MyView1
在别的地方就可以直接从views module导入 MyView1 了
from views import MyView1

###修改项目设置和url设置

####project/urls.py 中include新app的urls配置
```python
urlpatterns = [
    url(r'^$', login, name="login"),
    url(r'^attendence/', include('attendence.urls')),
    url(r'^secu/', include('secu.urls')),
    url(r'^cg/', include('cg.urls')),
]
```

####project/settings.py中配置新app为Installed
```python
INSTALLED_APPS = [
    'App1.apps.App1Config',
    'App2.apps.App2Config',    

    'MyApp1.apps.MyApp1Config',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

###完成
可以开始业务代码了