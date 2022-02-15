import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoMultipleWindows():
    def multiple_windows(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element_by_xpath("//a[@href='https://www.yatra.com/travel-guidelines/international/germany']//div[@class='imgRes']//img").click()
        time.sleep(3)
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath("//a[@href='https://www.yatra.com/offer/details/yatra-assure-program']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element_by_xpath(
            "//a[@href='https://www.yatra.com/travel-guidelines/international/germany']//div[@class='imgRes']//img").click()

mw = DemoMultipleWindows()
mw.multiple_windows()





