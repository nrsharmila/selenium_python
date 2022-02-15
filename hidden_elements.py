import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class demo_hidden_element():
    def hidden_element(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element_by_xpath("//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(elem1)

    def hidden_element_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element_by_xpath("//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elem2 = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(elem2)
demodisplayed = demo_hidden_element()
demodisplayed.hidden_element_yatra()



