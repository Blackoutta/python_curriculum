现在我们基本上就是在通过python遥控网页，下方的代码是在点击页面上的元素
--------------------------------------------------------------------------------
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://i.cqevi.net.cn/zfca/login')

# 首先找到想要点击的元素并做成对象
link_element = browser.find_element_by_css_selector("#username")
# 然后通过.click()方法点击即可
link_element.click()
