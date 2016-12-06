#ubuntu下在apache部署python站点

我的是ubuntu14 32为的虚拟机，默认安装的python为3.4
环境：apache + mysql + django + python3

####软件安装

```
#apache
sudo apt-get install apache2

#wsgi Python2
sudo apt-get install libapache2-mod-wsgi

#wsgi python3
sudo apt-get install libapache2-mod-wsgi-py3

#mysql
sudo apt-get install mysql-server mysql-client

#pip的安装有多种方式

#pip - 方法一
1. 官网下载 get-pip.py
2. python3 get-pip.py3

#pip - 方法二
#python2
sudo apt-get install python-pip
#python3
sudo apt-get install python3-pip

#python3下使用pip3
pip3 install pymysql
pip3 install django==1.9
pip3 install virturlenv

#python2
#mysql driver for python
pip install pymysql
pip install django==1.9
pip install virtualenv

```

#辅助工具的安装

修改配置文件用到编辑器，看喜好

```
#vim
sudo apt-get install vim

#sublime text 
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer

```


#apache网站的配置和部署

####httpd.conf中配置需要监听的端口

```
listen 80
listen 8000
```

####linux下多站点的配置
vhost.conf

```xml
<VirtualHost *:9090>
      # ServerName www.example.com
  
      ServerAdmin webmaster@localhost
      DocumentRoot /var/www/html
 
      ErrorLog ${APACHE_LOG_DIR}/error.log
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  
      Alias /static /home/ubuntu/wechat/static
      <Directory /home/ubuntu/wechat/static>
          Require all granted
      </Directory>
  
      <Directory /home/ubuntu/wechat/wechat>
          <Files wsgi.py>
              Require all granted
          </Files>
      </Directory>
  
      WSGIDaemonProcess wechat python-path=/home/ubuntu/wechat:/home/ubuntu/wechat/env/lib/python3.4/site-packages
      WSGIProcessGroup wechat
      WSGIScriptAlias / /home/ubuntu/wechat/wechat/wsgi.py
</VirtualHost>
```

####激活网站

```
sudo a2ensite mysite.conf
```