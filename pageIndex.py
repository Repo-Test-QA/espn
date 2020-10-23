from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndex:

    def __init__(self, my_driver):
        self.button = (By.ID, 'global-user-trigger')
        self.driver = my_driver

    def user(self):
        try:
            user_button = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.button))
            user_button.click()
        except:
            print('No se encuentra el elemento 1')
