print("----------------Brief Tour of the Standard Library----------------")

# import os
# os.getcwd()      # Return the current working directory
# # 'C:\\Python35'
# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell

import random
random.choice(['apple', 'pear', 'banana'])
# 'apple'
random.sample(range(100), 10)   # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random()    # random float
# 0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
# 2

# Internet Access
import io  
import sys  
import urllib.request  
# 设置python的默认编码 gb18030
# gb18030 和 gb2312 的区别？？？
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码 

from urllib.request import urlopen
if(1==2):
    with urlopen('http://www.cnblogs.com/') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
            if 'oracle' in line or 'java' in line:  # look for Eastern Time
                print(line)

# send email
# pass: 'anscbxwbmsotxxzh'//网易的授权码
import smtplib
smtpObj = smtplib.SMTP()
sender = "trad212remind@sina.com"
au_pwd='123456'
receivers = ["wancy86@126.com","461151239@qq.com"]
message = """"From: Mark <trad212remind@sina.com>
    To: wancy86 <wancy86@126.com>
    Subject: test email for python
    
    this is a test email.
    """
if(1==2):
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.sina.com", "25") 
        # 千万请注意下面的password是授权密码，不是邮箱的密码。
        # 授权密码需要在163邮箱设置中设置。
        state = smtpObj.login(sender, au_pwd)
        if state[0] == 235:
            smtpObj.sendmail(sender, receivers, message)
            print("send email success")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(str(e))

# 
import datetime
print(datetime.date(2003, 12, 2))

