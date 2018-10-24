from selenium import webdriver
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

schedule_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "129363840000054930")))
schedule_element.click()
