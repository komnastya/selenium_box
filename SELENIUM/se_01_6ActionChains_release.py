# release method is used for releasing a held mouse button on an element.
# Syntax: release(on_element=None).
import pathlib
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
action = ActionChains(driver)

five = driver.find_element_by_id('five')
action.click(five)
action.release(five)
action.perform()

time.sleep(2)

driver.close()
