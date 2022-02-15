import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoCheckboxes():
    def Checkbox(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.find_element_by_id('interest_market_c0').click()
        driver.maximize_window()
        var1 = driver.find_element_by_id('interest_market_c0').is_selected()
        print(var1)

        time.sleep(5)

var = DemoCheckboxes()
var.Checkbox()