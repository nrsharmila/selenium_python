import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoCaptureScreenshot():
    def capture_screenshot(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        continuedemo.click()

        time.sleep(2)

screenshot = DemoCaptureScreenshot()
screenshot.capture_screenshot()