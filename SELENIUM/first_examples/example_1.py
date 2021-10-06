from selenium.webdriver import Chrome  # Operating in headless mode
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.get('https://www.techwithtim.net/')

search = driver.find_element_by_name("s")  # find element by name
search.send_keys("Test")  # fill in the field
search.send_keys(Keys.RETURN)  # press enter buttom

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")) # wait for the entire part be downloaded
    )
    articles = main.find_elements_by_tag_name("article") # search for each <article> tag in the <main> part -> list
    for article in articles:
        header = article.find_element_by_class_name("entry-summary") # search for each <entry_summer> part in each article
        print(header.text)
finally:
    driver.quit()
