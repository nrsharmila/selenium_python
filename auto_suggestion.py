import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DemoAutoSuggestion():
    def Auto_suggestion(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(3)
        Depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        Depart_from.click()
        time.sleep(3)
        Depart_from.send_keys("New Delhi")
        time.sleep(3)
        Depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break

        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(3)
        # driver.find_element(By.ID, "08/02/2022").click()
        # time.sleep(3)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        print(all_dates)
           # for date in all_dates():
           #   if date.get_attribute("date-date") == "30/03/2022":
           #      date.click()
           #        time.sleep(3)
           #        break




depart = DemoAutoSuggestion()
depart.Auto_suggestion()