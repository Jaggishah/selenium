from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
button= driver.find_element(By.XPATH,"//*[@id='tabButton']") 
button.click()

windows = driver.window_handles

print(windows[0])
print(windows[1])

parent_window = windows[0]

driver.switch_to.window(parent_window)
sleep(6)
driver.quit()