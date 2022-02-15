import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class DemoDragandDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
        elem1 = driver.find_element_by_id("draggable")
        elem2 = driver.find_element_by_id("droppable")
        ActionChains(driver).drag_and_drop(elem1, elem2).perform()




        time.sleep(4)

var = DemoDragandDrop()
var.drag_drop()