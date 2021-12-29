# https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))

form = driver.find_element_by_id("states")
states_in_form = form.find_elements_by_tag_name("option")

# This function can be written in another module and be imported when we need it for testing:
def count_options_in_form(options):
    output = []
    count = 0
    for option in options:
        time.sleep(1)
        count += 1
        value = option.get_attribute("value")
        print(f"The {count}-th state in the list is: ", value)
        output.append(value)
        option.click()
    return output, count


lst_of_states, quantity_of_states = count_options_in_form(states_in_form)

driver.close()


def test_list_of_states():
    assert lst_of_states == ['Alabama', 'Alaska', 'Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Hawaii',
                      'Kansas', 'Michigan']
    assert len(lst_of_states) == quantity_of_states
    assert len(lst_of_states) == 10
