刚才我们点击了用户名，现在我们来填写它。我们可以顺便把密码也填写掉，并提交。
--------------------------------------------------------------------------------
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://i.cqevi.net.cn/zfca/login')

# 获取、填写账号
account_element = browser.find_element_by_css_selector("#username")
account_element.click()
account_element.send_keys("填写账号") # .send_keys()方法可以往表单中发送字符串

# 获取、填写密码
password_element = browser.find_element_by_css_selector("#password")
password_element.click()
password_element.send_keys("填写密码")

# 提交表单
password_element.submit() # .submit()方法可以提交当前表单
