import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demogettext():
    def get_text(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
       # driver.find_element_by_link_text('Yatra for Business').click()
        text = driver.find_element_by_xpath("//p[normalize-space()='Germany']").text
        print(text)
        driver.maximize_window()
        time.sleep(5)

gettext = Demogettext()
gettext.get_text()