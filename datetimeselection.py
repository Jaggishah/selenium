from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click


datepicker_mon = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_mon.select_by_visible_text("Jun")

datepicker_year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1990")

datepicker_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in datepicker_date:
    if date.text == "23":
        datepicker_date.click()