import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Explicit wait

# An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
# Explicit waits are achieved by using webdriverWait class in combination with expected_conditions.

driver = webdriver.Chrome()

# A URL that delays loading
driver.get("http://toolsqa.com")

try:
    # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/img"))
    )
finally:
    # else quit
    driver.quit()

# This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10
# seconds. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.

# Expected Conditions –
# There are some common conditions that are frequently of use when automating web browsers. For example,
# presence_of_element_located, title_is, ad so on:

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# etc.


with webdriver.Chrome() as driver:
    driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Open new window"))
    )
    # click the element
    element.click()
