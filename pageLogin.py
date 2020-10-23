from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageLogin:
    def __init__(self, my_driver):
        self.user = (By.CSS_SELECTOR, "input[type='email']")
        self.password = (By.CSS_SELECTOR, "input[type='password']")
        self.connect = (By.CSS_SELECTOR, "button. btn sign-up-btn-2 btn-block [type = submit]")
        self.driver = my_driver

    def enter_credential(self, user, password):
        try:
            enter_user = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.user))
            enter_user.send_keys(user)
            enter_password = WebDriverWait(self.password, 4).until(EC.visibility_of_element_located(self.password))
            enter_password.send_keys(password)
            click_button = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.connect))
            click_button.click()

        except:
            print('No se encuentra el elemento 3')