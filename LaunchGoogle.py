from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.maximize_window()
driver.close()