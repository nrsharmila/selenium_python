import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoRadiobutton():
    def Radio_button(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.find_element_by_id('doi0').click()
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_id('doi1').click()

        time.sleep(5)

var = DemoRadiobutton()
var.Radio_button()