import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# In this example it is possible to select more than one element simply by click on them:
driver.get("https://demoqa.com/selectable")

one = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[1]')
two = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[2]')
three = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[3]')
four = driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[4]')

actions = ActionChains(driver)
actions.click(one)
actions.click(two)
actions.click(three)
actions.click(four)

actions.perform()

# In this example we need to press Ctrl in order to select more than one element:
driver.get("C:/Users/root/Projects/selenium_box/selectable.html")

time.sleep(2)
one = driver.find_element_by_name('one')
two = driver.find_element_by_name('two')
three = driver.find_element_by_name('three')
four = driver.find_element_by_name('four')
five = driver.find_element_by_name('five')

# The next line presses the CONTROL button and holds it:

actions2 = ActionChains(driver)
actions2.key_down(keys.Keys.CONTROL)
actions2.click(one)
actions2.click(two)
actions2.click(three)
actions2.click(four)
actions2.click(five)

actions2.perform()

driver.close()
