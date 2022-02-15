import time
import selenium.webdriver.common.action_chains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class DemoMouseHover():
    def mouse_hover(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton = driver.find_element_by_xpath("//span[@class='more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(2)
        driver.find_element_by_xpath("//span[normalize-space()='Trains']").click()
        time.sleep(3)

demo = DemoMouseHover()
demo.mouse_hover()






