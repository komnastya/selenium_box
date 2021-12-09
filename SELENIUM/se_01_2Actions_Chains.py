import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# In this example it is possible to select more than one element simply by click on them:
driver.get("https://demoqa.com/selectable")

actions = ActionChains(driver)
actions.click(driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[1]'))
actions.click(driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[2]'))
actions.click(driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[3]'))
actions.click(driver.find_element_by_xpath('//*[@id="verticalListContainer"]/li[4]'))

actions.perform()

# In this example we need to press Ctrl in order to select more than one element:
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))

time.sleep(2)

actions2 = ActionChains(driver)

# The next line presses the CONTROL button and holds it:
actions2.key_down(keys.Keys.CONTROL)
actions2.click(driver.find_element_by_id('one'))
actions2.click(driver.find_element_by_id('two'))
actions2.click(driver.find_element_by_id('three'))
actions2.click(driver.find_element_by_id('four'))
actions2.click(driver.find_element_by_id('five'))

actions2.perform()

driver.close()
