# https://selenium-python.readthedocs.io/navigating.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# NAVIGATING

# The first thing you’ll want to do with WebDriver is navigate to a link. The normal way to do this is by calling get
# method:

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# WebDriver will wait until the page has fully loaded (that is, the onload event has fired) before returning control
# to your test or script. If you need to ensure such pages are fully loaded then you can use waits.


# INTERACTING WITH THE PAGE

# What we’d really like to do is to interact with the pages, or, more specifically, the HTML elements within a page.
# First of all, we need to find one. WebDriver offers a number of ways to find elements. For example, given an element
# defined as:

# <input type="text" name="passwd" id="passwd-id" />

# you could find it using any of:

# <input id="input" type="search" name="q" ... placeholder="Search Google or type a URL">

# element = driver.find_element_by_id("input")
element = driver.find_element_by_name("q")
# element = driver.find_element_by_xpath("//input[@id='input']")
# element = driver.find_element_by_css_selector("input#input")

# You can also look for a link by its text, but be careful! The text must be an exact match! You should also be
# careful when using XPATH in WebDriver. If there’s more than one element that matches the query, then only the
# first will be returned. If nothing can be found, a NoSuchElementException will be raised.

# WebDriver has an “Object-based” API; we represent all types of elements using the same interface. This means that
# although you may see a lot of possible methods you could invoke when you hit your IDE’s auto-complete key combination,
# not all of them will make sense or be valid. Don’t worry! WebDriver will attempt to do the Right Thing, and if you
# call a method that makes no sense (“setSelected()” on a “meta” tag, for example) an exception will be raised.

# So, you’ve got an element. What can you do with it? First of all, you may want to enter some text into a text field:
element.send_keys("some text")

# You can simulate pressing the arrow keys by using the “Keys” class:
element.send_keys(" and some", Keys.ARROW_DOWN)

# It is possible to call send_keys on any element, which makes it possible to test keyboard shortcuts such as those
# used on GMail. A side-effect of this is that typing something into a text field won’t automatically clear it.
# Instead, what you type will be appended to what’s already there. You can easily clear the contents of a text field or
# textarea with the clear method:

element.clear()

driver.close()
