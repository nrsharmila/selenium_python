import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demogetattribute():
    def get_attribute_value(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute('id')
        print(attr_value)
        driver.maximize_window()
        time.sleep(5)

attrobj = Demogetattribute()
attrobj.get_attribute_value()