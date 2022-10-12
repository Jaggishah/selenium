from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os

location = os.getcwd()

perferences = {"download.default_directory":location}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs",perferences)

driver = webdriver.Chrome()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()