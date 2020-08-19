from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

web = webdriver.Firefox()
web.get("https://mail.qq.com")
#
# xpath = web.find_element_by_xpath("//*[@id='login']")

web.switch_to.frame('login_frame')

web.find_element_by_xpath('//*[@id="u"]').send_keys("434897575")


web.find_element_by_xpath('//*[@id="p"]').send_keys("ywj19990625...")


web.find_element_by_xpath('//*[@id="login_button"]').click()

web.switch_to.default_content()

time.sleep(5)

web.find_element_by_css_selector("#composebtn").click()

web.switch_to.frame(1)

web.find_element_by_xpath('//*[@id="toAreaCtrl"]/div/input').send_keys("370801466@qq.com")

web.find_element_by_id("subject").send_keys("哦吼")

time.sleep(2)

web.switch_to.frame(0)

web.find_element_by_css_selector("body").send_keys("高伟光真帅")

time.sleep(2)

web.switch_to.parent_frame()

web.find_element_by_css_selector("#frm > div:nth-child(12) > div:nth-child(1) > a:nth-child(2)").click()

time.sleep(100)

web.quit()



