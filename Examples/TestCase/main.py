import unittest
from selenium.webdriver import Chrome
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("http://www.python.org/")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_botton()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def TearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
