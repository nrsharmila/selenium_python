import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementBytagname():
    def locate_by_id(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element_by_tag_name('input').send_keys('test@test.com')
        driver.find_element_by_class_name('email-login-box').send_keys('test@test.com')
        time.sleep(5)

findbytagname = DemoFindElementBytagname()
findbytagname.locate_by_id()