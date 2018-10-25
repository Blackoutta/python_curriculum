现在我们的脚本已经可以帮助我们自动登录。
但是我们如果尝试直接在新页面中点击某个元素的话，程序会有可能会崩溃，因为网页的加载一般不会这么快。
所以我们需要修改一些东西，来让程序等待新网页加载出想要的元素后，再点击它。
这个解决方法是在Stack Overflow找到的： https://stackoverflow.com/questions/37787453/selenium-python-how-to-wait-for-a-page-to-load-after-a-click
--------------------------------------------------------------------------------
from selenium import webdriver
# 从 selenium中又导入了三个功能，都与等待相关
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://i.cqevi.net.cn/zfca/login')

account_element = browser.find_element_by_css_selector("#username")
account_element.click()
account_element.send_keys("填写账号")

password_element = browser.find_element_by_css_selector("#password")
password_element.click()
password_element.send_keys("填写密码")
password_element.submit()

# 运用导入的功能，让浏览器先等待ID为129363840000054930的元素被加载出来，然后再将它做成对象
schedule_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "129363840000054930")))
schedule_element.click()
