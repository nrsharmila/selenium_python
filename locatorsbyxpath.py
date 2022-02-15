import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByXpath():
    def locate_by_id(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_xpath("//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(5)

findbyxpath = DemoFindElementByXpath()
findbyxpath.locate_by_id()