from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")

button = driver.find_element(By.XPATH,"//input[@type='submit' and @class='wikipedia-search-button']")
button.click()

links = driver.find_element(By.XPATH,"//*[@id='wikipedia-search-result-link']/a")
links.click()
# for li in links:
#    print(li.text)
   
