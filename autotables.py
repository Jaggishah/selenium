from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
header = driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th")
noofrows = driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr")
# columndata = driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr/td")

# below code just for heading
# for i in range(1,len(header)+1):
#     headerstext = driver.find_element(By.XPATH,f"//*[@id='customers']/tbody/tr[1]/th[{i}]")
#     print(headerstext.text)

for i in range(2,len(noofrows)+1):
    for j in range(1,len(header)+1):
        data = driver.find_element(By.XPATH,f"//*[@id='customers']/tbody/tr[{i}]/td[{j}]")
        print(data.text,end="\t")

    print( )

