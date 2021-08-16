import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
# TC02


class TestLogin(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def test_tc02_login(self):
        self.driver.get("http://localhost:1667/")
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("ntest2@ceg.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("ntest222A")
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(2)
        assert self.driver.find_element_by_link_text("ntest2").text == "ntest2"
        self.driver.find_element_by_link_text("Log out").click()
        time.sleep(2)
