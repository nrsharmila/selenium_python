import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Demoright_double_click():
    def double_click(self):
         driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
         driver.get("https://demo.guru99.com/test/simple_context_menu.html")
         driver.maximize_window()
         elem = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
        #copyelem = driver.find_element_by_xpath("ex:that element of xpath")
         rc = ActionChains(driver)
         rc.context_click(elem).perform()
         time.sleep(3)
        #copyelem.click()
        #time.sleep(2)

         # elem1 = driver.find_element_by_xpath("//button[normalize-space()='Double-Click Me To See Alert']")
         # dc = ActionChains(driver)
         # dc.double_click("elem1").perform()
         # time.sleep(3)





demo = Demoright_double_click()
demo.double_click()