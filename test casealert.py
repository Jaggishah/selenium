from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()

myalert = driver.switch_to.alert
print(myalert.text)
myalert.accept()