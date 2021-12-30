import time

from selenium import webdriver

# Navigation

with webdriver.Chrome() as driver:
    driver.get('https://www.selenium.dev/documentation/webdriver/')

    element = driver.find_element_by_link_text('Elements')

    time.sleep(3)
    element.click()

    time.sleep(3)
    # Go back:
    driver.back()

    time.sleep(3)
    # Go forward:
    driver.forward()

    time.sleep(3)
    # Refresh page:
    driver.refresh()
