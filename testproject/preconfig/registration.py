import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.headless = True


class TestRegistration(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def teardown_method(self):
        self.driver.quit()

    def test_registration(self):
        self.driver.get("http://localhost:1667/")
        time.sleep(2)
        self.driver.find_element_by_link_text("Sign up").click()
        self.driver.find_element_by_xpath('//input[@type="text"]').send_keys("ntest2")
        self.driver.find_element_by_xpath('(//input[@type="text"])[2]').send_keys("ntest2@ceg.hu")
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys("ntest222A")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign up\')]").click()
        time.sleep(6)
        reg = self.driver.find_elements_by_xpath('//div[text()="Your registration was successful!"]')
        assert len(reg) > 0
        self.driver.find_element(By.XPATH, "//button[contains(.,\'OK\')]").click()
        elements = self.driver.find_elements_by_link_text("ntest2")
        assert len(elements) > 0
        self.driver.find_element_by_link_text("Log out").click()
