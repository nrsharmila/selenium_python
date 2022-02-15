import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoJsExecution():
    def js_execution(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        #driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")

        driver.maximize_window()


        time.sleep(3)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(5)

var = DemoJsExecution()
var.js_execution()