import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByLinkText():
    def locate_by_linktext(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
       # driver.find_element_by_link_text('Yatra for Business').click()
        driver.find_element_by_partial_link_text('Yatra for').click()
        driver.maximize_window()
        time.sleep(10)

findbylinktext = DemoFindElementByLinkText()
findbylinktext.locate_by_linktext()