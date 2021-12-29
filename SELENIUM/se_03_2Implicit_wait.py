# An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or
# elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life
# of the WebDriver object.

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://selenium-python.readthedocs.io/index.html')
explicit = driver.find_element_by_partial_link_text('5.1. Explicit Waits')
explicit.click()
implicit = driver.find_element_by_partial_link_text('5.2. Implicit Waits')
implicit.click()

driver.close()

# This implicit wait is available for the all elements on the web-page (for get, explicit, implicit).
# We don't see the effect of implicit wait, if the page is loaded fast.
