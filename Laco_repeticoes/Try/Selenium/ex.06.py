from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

source_box = driver.find_element("name", "q")
source_box.send_keys("Automação com Python")
source_box.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()