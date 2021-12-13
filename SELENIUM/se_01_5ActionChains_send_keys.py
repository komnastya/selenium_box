# send_keys method is used to send keys to current focused element.
# syntax: send_keys(*keys_to_send)
import pathlib
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
action = ActionChains(driver)

time.sleep(1)
state = driver.find_element_by_id('states')
state.send_keys('Florida')

time.sleep(1)
five = driver.find_element_by_id('five')
five.click()

eight = driver.find_element_by_id('eight')
action.key_down(Keys.CONTROL).click(eight).perform()

action.reset_actions()
time.sleep(1)
address = driver.find_element_by_id('current')
address.send_keys('Minsk, Belarus')

time.sleep(2)

driver.close()
