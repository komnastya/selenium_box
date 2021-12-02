# ActionChains

# Selenium’s Python Module is built to perform automated testing with Python. ActionChains are a way to automate
# low-level interactions such as mouse movements, mouse button actions, keypress, and context menu interactions.

# To create object of Action Chain, import ACtion chain class from docs and pass driver as the key argument.
# After this one can use this object to perform all the operations of action0 chains.
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action0 = ActionChains(driver)
driver.get("https://jqueryui.com/")

# click method is used to click on an element or current position.
about = driver.find_element_by_xpath('//*[@id="menu-top"]/li[8]/a')
action0.click(on_element=about).perform()

# click_and_hold method is used to hold down the left mouse button on an element:
time.sleep(2)
action2 = ActionChains(driver)
demos = driver.find_element_by_xpath('//*[@id="menu-top"]/li[1]/a')
action2.click_and_hold(on_element=demos).perform()

# double_click method is used to double click on an element or current position:
time.sleep(2)
action3 = ActionChains(driver)
download = driver.find_element_by_xpath('//*[@id="menu-top"]/li[2]/a')
action3.double_click(download).perform()

#reset

time.sleep(2)
action = ActionChains(driver)
element = driver.find_element_by_xpath('//*[@id="menu-top"]/li[1]/a')
action.click(on_element=element)
action.perform()
another_element = driver.find_element_by_xpath('//*[@id="menu-top"]/li[2]/a')
action.reset_actions()
action.click(on_element=another_element)
action.perform()


# context_click method is used to perform a context-click (right click) on an element:
time.sleep(2)
action4 = ActionChains(driver)
blog = driver.find_element_by_xpath('//*[@id="menu-top"]/li[7]/a')
action4.context_click(blog).perform()
time.sleep(2)

driver.close()

# List of methods:
# drag_and_drop
# drag_and_drop_by_offset
# key_down
# key_up
# move_by_offset
# move_to_element
# move_to_element_with_offset
# perform
# pause
# release
# reset_actions
# send_keys
