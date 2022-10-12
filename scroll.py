from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get("https://jqueryui.com/slider/")
browser.execute_script("window.scrollTo(0,500)")

# ele = browser.find_element(By.XPATH,"//*[@id='legal']/ul/li[1]/a")
# browser.execute_script("arguments[0].scrollIntoView(true);", ele)
#                        "arguments[0].scrollIntoView(true);", element
# # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")