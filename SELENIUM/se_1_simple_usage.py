# https://selenium-python.readthedocs.io/getting-started.html

# The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver
# implementations are Firefox, Chrome, IE and Remote. The Keys class provide keys in the keyboard
# like RETURN, F1, ALT etc.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Next, the instance of Chrome WebDriver is created.
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully
# loaded (that is, the “onload” event has fired) before returning control to your test or script.
driver.get("http://www.python.org")

# The next line is an assertion to confirm that title has “Python” word in it:
assert "Python" in driver.title

# WebDriver offers a number of ways to find elements using one of the find_element_by_* methods:
elem = driver.find_element_by_name("q")

# Next, we are sending keys, this is similar to entering keys using your keyboard. Special keys can be sent using Keys
# class imported from selenium.webdriver.common.keys. To be safe, we’ll first clear any pre-populated text in the
# input field (e.g. “Search”) so it doesn’t affect our search results:
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# After submission of the page, you should get the result if there is any. To ensure that some results are found,
# make an assertion:
assert "No results found." not in driver.page_source

# Finally, the browser window is closed. You can also call quit method instead of close. The quit will exit entire
# browser whereas close will close one tab, but if just one tab was open, by default most browser will exit entirely:
driver.close()
