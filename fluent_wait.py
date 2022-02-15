import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DemoFluentWait():
    def handle_fluent_wait(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        Depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        Depart_from.click()

        Depart_from.send_keys("New Delhi")

        Depart_from.send_keys(Keys.ENTER)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[ElementClickInterceptedException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id = 'monthWrapper']//tbody//td[@class!='inActiveTD']"))).\
                find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates():
            if date.get_attribute("date-date") == "30/03/2022":
                date.click()
                time.sleep(3)
                break
demo = DemoFluentWait()
demo.handle_fluent_wait()