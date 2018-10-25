from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://i.cqevi.net.cn/zfca/login')

account_element = browser.find_element_by_css_selector("#username")
account_element.click()
account_element.send_keys("填写账号")

password_element = browser.find_element_by_css_selector("#password")
password_element.click()
password_element.send_keys("填写密码")
password_element.submit()
