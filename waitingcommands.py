from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")

link = driver.find_element(By.XPATH,"//input[@name='q']")
link.send_keys("Selenium")
link.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.close()