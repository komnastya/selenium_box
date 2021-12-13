import pathlib

from selenium import webdriver
from selenium.webdriver import ActionChains

# Pause method is used to pause all inputs for the specified duration in seconds. Pause method is highly important and
# useful in case one is executing some command that takes some javascript to load or a similar situation where there is
# a time gap between two operations.

# syntax: pause(seconds)

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
action = ActionChains(driver)

five = driver.find_element_by_id('five')
eight = driver.find_element_by_id('eight')

action.click(five)
action.pause(3)

action.click(eight)
action.pause(3)

action.perform()

driver.close()
