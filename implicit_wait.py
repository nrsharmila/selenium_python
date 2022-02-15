import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoImplicitwait():
    def implicit_wait(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.find_element_by_id('username').send_keys("Rcv academy")
        driver.find_element_by_id('password').send_keys("rcv academy")


var = DemoImplicitwait()
var.implicit_wait()