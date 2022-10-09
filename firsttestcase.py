from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://ultimateqa.com/automation')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input#subscribe-field-blog_subscription-2)").send_keys("Admin")
driver.close()