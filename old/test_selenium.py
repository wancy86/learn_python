from selenium import webdriver
# 创建一个chrome实例
driver = webdriver.Chrome()
#这个是制定google浏览器,
#指定IE webdriver       
#driver webdriver.Ie(),
#指定Firefox webdriver driver webdriver.Firefox()
 
# 到百度主页
driver.get("http://www.baidu.com")
# 定位到搜索输入框
inputElement = driver.find_element_by_xpath ("//input[@name='wd']")
# 输入查找内容
inputElement.send_keys("selenium python")
# 点击百度一下
submitElement.submit()
# 输出网页标题
print(driver.title)
#退出webdriver
driver.quit()
 
# 运行脚本会自动开启chrome自动开始测试