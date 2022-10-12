from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.implicitly_wait(4)

driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("jaggi shah")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").perform()