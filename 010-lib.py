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
server = smtplib.SMTP('smtp.126.com')
server.sendmail('wancy86@126.com', 'wancy86@126.com',
"""To: wancy86@126.org
From: wancy86@126.org

Beware the Ides of March.
""")
print('email sent..')
server.quit()

smtpObj = smtplib.SMTP()
sender = "wancy86@126.com"
pwd126='wancy86' #网易的授权码
receivers = ["451151239@qq.com"]
message = """From: Mark
    To: zoro <451151239@qq.com>
    Subject: test email from python
    
    this is a test email.

    Thank you,
    Mark
    """
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect("smtp.126.com", "25") 
    # 千万请注意下面的password是授权密码，不是邮箱的密码。
    # 授权密码需要在163邮箱设置中设置。
    state = smtpObj.login(sender, pwd126)
    if state[0] == 235:
        smtpObj.sendmail(sender, receivers, message)
        print("send email success")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print(str(e))