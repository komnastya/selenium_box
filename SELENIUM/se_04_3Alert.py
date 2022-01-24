import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    driver.get('https://demoqa.com/alerts')

    # Click the link to activate the alert:
    driver.find_element_by_id('alertButton').click()

    # Wait for the alert to be displayed and store it in a variable:
    alert = WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())

    # Store the alert text in a variable:
    text = alert.text
    assert text == 'You clicked a button'

    time.sleep(3)
    # Press the OK button:
    alert.accept()

    # CONFIRM

    time.sleep(3)
    # Click the other link to activate the alert:
    driver.find_element_by_id('confirmButton').click()

    # Wait for the alert to be displayed and store it in a variable:
    WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())

    # Store the alert in a variable for reuse:
    alert = driver.switch_to.alert

    # Store the alert text in a variable:
    text2 = alert.text
    assert text2 == 'Do you confirm action?'

    time.sleep(3)
    alert.accept()

    # Press the Cancel button:
    driver.find_element_by_id('confirmButton').click()
    time.sleep(3)
    alert.dismiss()

    # PROMPT

    # Click the other link to activate the alert:
    driver.find_element_by_id('promtButton').click()

    # Wait for the alert to be displayed
    WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())

    # Store the alert in a variable for reuse
    alert = Alert(driver)

    time.sleep(3)
    # Type your message
    alert.send_keys("Selenium")

    # Press the OK button
    alert.accept()

    time.sleep(3)
