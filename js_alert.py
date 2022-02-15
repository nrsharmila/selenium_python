import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoJsAlert():
    def js_alert(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element_by_xpath("//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.accept()




        time.sleep(3)

var = DemoJsAlert()
var.js_alert()