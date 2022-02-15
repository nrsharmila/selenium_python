import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementsBytagname():
    def locate_by_id(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/")
       # lista = driver.find_elements_by_tag_name('a')
        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)

        time.sleep(5)

findbytagname = DemoFindElementsBytagname()
findbytagname.locate_by_id()