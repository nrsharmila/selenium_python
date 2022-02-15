import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demoiframes():
    def i_frames(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        time.sleep(2)


        driver.find_element_by_xpath("//a[@title='Get Your Own Website With W3Schools Spaces']").click()

        time.sleep(3)

frames = Demoiframes()
frames.i_frames()