from xml.dom.minidom import Element
from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()

act = ActionChains(driver)

# find element

# act.double_click(Element).perform() for double click
act.context_click(Element).perform()  #for right click

# note: perform is must for all action chains method thanks

# act.drag_and_drop(target and destination).perform()
