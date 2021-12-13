# reset_actions method
import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome()

# get programiz.com
driver.get("https://programiz.com/")

# create action chain object
action = ActionChains(driver)

# get element
element = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[2]/a[1]/span')

# click the item
action.click(on_element=element)

# perform the operation
action.perform()

# reset the action
action.reset_actions()

time.sleep(2)
# wait for a new page to load

# get another element
element = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[2]/a[2]/span')

# click the item
action.click(on_element=element)

# perform the operation
action.perform()
