import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropDownSingleSelect():
    def DropDown_SingleSelect(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/au/form/demo/overview-demo/")
        driver.maximize_window()
        dropdown = driver.find_element_by_name("UserTitle").click()
        time.sleep(5)
        dd = Select(dropdown)
        dd.select_by_index(1)

        time.sleep(5)


var = DemoDropDownSingleSelect()
var.DropDown_SingleSelect()