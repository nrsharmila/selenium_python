import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver.get("https://training.rcvacademy.com")
# driver.current_url
# driver.back()
# driver.forward()
# driver.refresh()
# driver.title
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
# driver.close()
# driver.quit()


class DemoBrowserCommands():
    def browser_methods(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element_by_link_text('ALL COURSES').click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(5)
        driver.quit()

browsercommands = DemoBrowserCommands()
browsercommands.browser_methods()