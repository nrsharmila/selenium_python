import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class DemoSliders():
    def handle_sliders(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/mobiles-accessories?sort=plrty&q=Price%3A99%2C6399%7C")
        driver.maximize_window()
        time.sleep(2)

        elem1 = driver.find_element_by_xpath("//a[contains(@class, 'left-handle')]")
        elem2 = driver.find_element_by_xpath("//a[contains(@class, 'right-handle')]")
        #ActionChains(driver).drag_and_drop_by_offset(elem1, 40, 0).perform()
        ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50, 0).release().perform()




        time.sleep(4)

var = DemoSliders()
var.handle_sliders()