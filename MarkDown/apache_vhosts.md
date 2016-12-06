#apache多站点配置

临时需要个测试站，然后就到apache中配置vhosts，结果这货总是显示"拒绝了你的请求"，找半天发现居然还要添加端口监听

####vhosts.conf

添加vhost

```xml
<VirtualHost *:80>
    DocumentRoot "D:\wwwphp\test"
    ServerName test.cn
    ServerAlias 
  <Directory "D:\wwwphp\test">
      Options FollowSymLinks ExecCGI
      AllowOverride All
      Order allow,deny
      Allow from all
      Require all granted
  </Directory>
</VirtualHost>

<VirtualHost *:8000>
    DocumentRoot "D:\wwwphp\test2"
    ServerName test2.com
    ServerAlias 
  <Directory "D:\wwwphp\test2">
      Options FollowSymLinks ExecCGI
      AllowOverride All
      Order allow,deny
      Allow from all
      Require all granted
  </Directory>
</VirtualHost>
```

####httpd.conf

所有的端口都要添加监听，记得之前配置没让配置这个
```
#Listen 12.34.56.78:80
Listen 80
Listen 8000
```