import pathlib
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# SELECT CLASS

driver = webdriver.Chrome()
driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))

# Find id of option:
select_form = driver.find_element_by_id('states')
drop_list = Select(select_form)

time.sleep(1)

# Select the option by value:
drop_list.select_by_value('AL')  # Alabama

time.sleep(1)

# Select the option by index:
drop_list.select_by_index(1)  # 2 Alaska

time.sleep(1)

# Select the option by its text:
drop_list.select_by_visible_text('Arizona')

time.sleep(1)

# Return a list of options that the <select> element contains:
options = drop_list.options

# Return a list of options that have been selected:
all_selected_options = drop_list.all_selected_options

# Return a WebElement referencing the first selection option found by walking down the DOM:
first_selected_option = drop_list.first_selected_option

# Deselect the option by value:
drop_list.deselect_by_value('AL')  # Alabama

time.sleep(1)

# Deselect the option by index:
drop_list.deselect_by_index(1)  # 2 Alaska

time.sleep(1)

# Deselect the option by its text:
drop_list.deselect_by_visible_text('Arizona')

time.sleep(1)

# # Deselect all selected <option> elements:

drop_list.select_by_value('AL')
drop_list.select_by_value('AK')
drop_list.select_by_value('CA')

time.sleep(1)
drop_list.deselect_all()
time.sleep(1)

assert drop_list.is_multiple is True

driver.close()

print('\nAll options: ', options)
print('\nAll selected options', all_selected_options)
print('\nFirst selected options', first_selected_option)
