import pathlib

from selenium import webdriver
from selenium.webdriver import ActionChains

# move_to_element method is used to move the mouse to the middle of an element.
# syntax: move_to_element(to_element)

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
action = ActionChains(driver)

five = driver.find_element_by_id('five')

action.pause(1).move_to_element(five).pause(2)
action.reset_actions()

# move_by_offset method is used for moving the mouse to an offset from current mouse position.
# syntax: move_by_offset(xoffset, yoffset)

# xoffset: X offset to move to, as a positive or negative integer.
# yoffset: Y offset to move to, as a positive or negative integer.

action.move_by_offset(100, 0).pause(2)
action.reset_actions()

# move_to_element_with_offset method is used to move the mouse by an offset of the specified element. Offsets are relative to the top-left corner of the element.
# syntax: move_to_element_with_offset(to_element, xoffset, yoffset)
# args:
# to_element: The WebElement to move to.
# xoffset: X offset to move to.
# yoffset: Y offset to move to.

seven = driver.find_element_by_id('seven')
action.move_to_element_with_offset(seven, 150, 100).pause(2)

action.perform()

driver.close()
