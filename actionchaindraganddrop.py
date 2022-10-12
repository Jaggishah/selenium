from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(10)

src = driver.find_element(By.XPATH,"//div[@id='box6']")
desn = driver.find_element(By.XPATH,"//div[@id='box106']")




act  = ActionChains(driver)

act.drag_and_drop(src,desn).perform()
# for second box
src2 = driver.find_element(By.XPATH,"//div[@id='box3']")
desn2 = driver.find_element(By.XPATH,"//div[@id='box103']")

act.drag_and_drop(src2,desn2).perform()