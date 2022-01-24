import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:

    # Open page
    driver.get(str(pathlib.Path(__file__).parent / 'tests.html'))

    # Store the ID of the original window, which is tests.html
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "Open new window").click()

    # Wait for the new window or tab
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    WebDriverWait(driver, 10).until(EC.title_is("Test2"))

    time.sleep(3)

    # Come back to original window
    driver.switch_to.window(original_window)
    time.sleep(3)
