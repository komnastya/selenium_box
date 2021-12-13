import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# key_down method is used to send a key press, without releasing it.
# This method is used in case one wants to press, ctrl+c, or ctrl+v.
# For this purpose one needs to first hold the ctrl key down and then press c.
# This method automates this work. It should only be used with modifier keys (Control, Alt and Shift).

# key_up method is used to release a pressed key using key_down method.

# syntax:
# key_down(value, element=None)
# key_up(value, element=None)

# value: The modifier key to send. Values are defined in Keys class.
# element: The element to send keys. If None, sends a key to current focused element.

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
action = ActionChains(driver)

element = driver.find_element_by_id('current')
element.send_keys('Pervomayskya 23/30')
action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

time.sleep(3)

another = driver.find_element_by_id('permanent')
action.key_down(Keys.CONTROL, element=another).send_keys('V').key_up(Keys.CONTROL).perform()

time.sleep(3)
driver.close()
