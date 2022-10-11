from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ui.vision/demo/webtest/frames/")
frame1 = driver.find_element(By.XPATH,"//html/frameset/frame[1]")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//*[@id='id1']/div/input").send_keys("jaggi")

driver.switch_to.parent_frame() #defaultcontent

frame2 = driver.find_element(By.XPATH,"/html/frameset/frameset/frame[3]")
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,"//*[@id='id4']/div/input").send_keys("shah")

