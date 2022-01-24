import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get(str(pathlib.Path(__file__).parent / 'tests2.html'))

    # There are three ways to switch to frame:

    # 1. Switching using a WebElement is the most flexible option.
    # You can find the frame using CSS selector and switch to it:

    # Store iframe web element
    iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

    # Switch to selected iframe
    driver.switch_to.frame(iframe)

    # Now click on button -> go to "Documentation" page
    driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(4) > a > span').click()

    time.sleep(3)

    # To leave an iframe or frameset, switch back to the default content like so:
    driver.switch_to.default_content()

    # 2. If your frame or iframe has an id or name attribute, this can be used instead.
    # If the name or ID is not unique on the page, then the first one found will be switched to.
    driver.switch_to.frame('buttonframe')

    # Now click on button -> go to main page
    driver.find_element_by_id('selenium_logo').click()

    # To leave an iframe or frameset, switch back to the default content like so:
    driver.switch_to.default_content()
    time.sleep(3)

    # 3. It is also possible to use the index of the frame, such as can be queried using window.frames in JavaScript.
    # switching to second iframe based on index
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(5) > a > span').click()

    time.sleep(3)
