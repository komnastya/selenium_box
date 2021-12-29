import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Custom Wait Conditions

# It is possible to create custom wait conditions when none of the previous convenience methods fit your requirements.
# A custom wait condition can be created using a class with __call__ method which returns False when the condition
# doesn’t match.


class element_has_css_class(object):
    """An expectation for checking that an element has a particular css class.

    locator - used to find the element
    returns the WebElement once it has the particular css class
    """

    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False


driver = webdriver.Chrome()

driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
wait = WebDriverWait(driver, 10)

# Wait until an element with id='one' has class 'ui-state-default'
element = wait.until(element_has_css_class((By.ID, 'one'), "ui-state-default"))
time.sleep(5)
driver.close()
