import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import yaml

class DemoFindElementState():
    def web_element_state(self):
        read_config = read.yaml('config.yaml')

        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.facebook.com/")
        driver.get(read_config['input']['website'])
        element_state = driver.find_element_by_tag_name("button").is_enabled()
        print(element_state)
        time.sleep(5)
        if element_state is True:
            print(status)

elementstateobj = DemoFindElementState()
elementstateobj.web_element_state()





