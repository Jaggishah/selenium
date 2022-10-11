from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

# alldrpdwon = Select(driver.find_element(By.XPATH,"//select"))

# # alldrpdownoptions = alldrpdwon.options
# # c =0 
# # for drp in alldrpdwon:
# #     c+=1
# #     print(c,":",drp.text,end=" ")

# alldrpdwon.select_by_visible_text('Austria')
# driver.quit()

drpdown = driver.find_elements(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select//option")
for drp in drpdown:
    if drp.text == "Austria":
        drp.click()
