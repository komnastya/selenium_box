# https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get("C:/Users/root/Projects/selenium_box/tests.html")

element = driver.find_element_by_xpath("//*[@id='states']")
all_options = element.find_elements_by_tag_name("option")

states = []
count = 0

# example from the tutorial:
for option in all_options:
    time.sleep(1)
    count += 1
    print(f"The {count}-th state in the list is: ", option.get_attribute("value"))
    states.append(option.get_attribute("value"))
    option.click()

driver.close()

expected_result = ['Alabama', 'Alaska', 'Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Hawaii', 'Kansas',
                   'Michigan']
result = states

def test_list_of_states():
    assert result == expected_result
