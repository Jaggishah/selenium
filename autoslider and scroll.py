from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(10)

act  =ActionChains(driver)

frame = driver.find_element(By.XPATH,"//*[@id='content']/iframe")

driver.switch_to.frame(frame)
slider = driver.find_element(By.XPATH,"//span[@tabindex='0']")
print(slider.location)

act.drag_and_drop_by_offset(slider,100,0).perform()

# time.sleep(4)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

ele = driver.find_element(By.XPATH,"//*[@id='legal']/ul/li[1]/a")
# driver.execute_script("argument[0],scrollIntoView();",ele)