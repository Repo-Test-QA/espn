from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PagePreLogin:
    def __init__(self, my_driver):
        self.enter_button = (By.CSS_SELECTOR, "a[data-affiliatename='espn']")
        self.driver = my_driver

    def enter(self):
        try:
            user_enter = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.enter_button))
            user_enter.click()
        except:
            print('No se encuentra el elemento 2')