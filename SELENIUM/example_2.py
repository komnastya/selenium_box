# https://selenium-python.readthedocs.io/getting-started.html#using-selenium-to-write-tests
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# USING SELENIUM TO WRITE TEST
# The selenium package itself doesn’t provide a testing tool/framework. You can write test cases using Python’s
# unittest or pytest module.


class PythonOrgSearch(unittest.TestCase):

    # The setUp is part of initialization, this method will get called before every test function which you are going
    # to write in this test case class. Here you are creating the instance of Chrome WebDriver.
    def setUp(self):
        self.driver = webdriver.Chrome()

    # This is the test case method. The first line inside this method create a local reference to the driver object
    # created in setUp method:
    def test_search_in_python_org(self):
        driver = self.driver

        # The driver.get method will navigate to a page given by the URL:
        driver.get("http://www.python.org")

        # The next line is an assertion to confirm that title has “Python” word in it:
        self.assertIn("Python", driver.title)

        # This way we find the element by its name:
        elem = driver.find_element_by_name("q")

        # Here we are sending key, simulating the user's behaviour:
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)

        # This assertions ensures that some result has been found:
        assert "No results found." not in driver.page_source

    # The tearDown method will get called after every test method. This is a place to do all cleanup actions.
    # In the current method, the browser window is closed.
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
