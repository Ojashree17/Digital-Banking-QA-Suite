from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://parabank.parasoft.com/parabank/index.htm")

driver.maximize_window()

driver.find_element(By.NAME, "username").send_keys("john")
driver.find_element(By.NAME, "password").send_keys("demo")

driver.find_element(By.XPATH, "//input[@value='Log In']").click()

time.sleep(5)

driver.quit()


