from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
import time
from pageIndex import PageIndex
from pagePreLogin import PagePreLogin
from pageLogin import PageLogin


class TestCase(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        #option.add_argument('incognito')

        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('https://www.espn.com/?src=com&amp;_adblock=true')
        self.driver.implicitly_wait(5)

        self.indexPage = PageIndex(self.driver)
        self.indexPagePreLogin = PagePreLogin(self.driver)
        self.indexPageLogin = PageLogin(self.driver)

    def test_login(self):
        self.indexPage.user()
        self.indexPagePreLogin.enter()
        self.indexPageLogin.enter_credential('guidosjulca@gmail.com', '#Arica01')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



