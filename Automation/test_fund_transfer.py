from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://parabank.parasoft.com/parabank/index.htm")

driver.maximize_window()

# Login
driver.find_element(By.NAME, "username").send_keys("john")
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

time.sleep(3)

# Transfer Funds
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

time.sleep(2)

driver.find_element(By.ID, "amount").send_keys("100")

driver.find_element(By.XPATH, "//input[@value='Transfer']").click()

time.sleep(5)

driver.quit()