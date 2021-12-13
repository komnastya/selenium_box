import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# drag_and_drop method holds down the left mouse button on the source element, then moves to the target element and
# releases the mouse button.

# drag_and_drop_by_offset holds down the left mouse button on the source element, then moves to the target offset and
# releases the mouse button.

# Syntax: drag_and_drop(source, target)
# source: The element to mouse down.
# target: The element to mouse up.

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')
action = ActionChains(driver)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

elem1 = driver.find_element_by_id('draggable')
elem2 = driver.find_element_by_id('droppable')

action.drag_and_drop(elem1, elem2).perform()
action.drag_and_drop_by_offset(elem1, -200, 0).perform()  # move the second time using x and y coordinates (moving is
# relative to current position

time.sleep(2)

driver.close()
