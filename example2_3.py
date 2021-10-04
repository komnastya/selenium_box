import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys  # Keys class provides keys in the keyboard like RETURN, F1, ALT etc.

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):  # The setUp is part of initialization, this method will get called before every test function
        self.driver = Chrome()  # create browser instance

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")   # The driver.get method will navigate to a page given by the URL.
        # WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before
        # returning control to your test or script.
        self.assertIn("Python", driver.title)  # the assertion confirms that title has “Python” word in it
        elem = driver.find_element_by_name("q")  # find the 'search' field
        elem.send_keys("pycon")  # enter 'pycon' in the 'search' field
        elem.send_keys(Keys.RETURN)  # press 'enter'
        assert "No results found." not in driver.page_source  # ensures that some results are found


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
