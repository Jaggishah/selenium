from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://www.google.com/")
link = driver.find_element(By.XPATH,"//input[@name='q']")
link.send_keys("Selenium")
link.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
searchlink = mywait.until(ec.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()