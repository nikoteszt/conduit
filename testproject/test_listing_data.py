import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True


class TestListingData(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:1667/")
        time.sleep(3)
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("ntest2@ceg.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("ntest222A")
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(3)
        assert len(self.driver.find_elements_by_link_text('ntest2')) > 0

    def teardown_method(self):
        self.driver.find_element_by_link_text("conduit").click()
        self.driver.find_element_by_link_text("Log out").click()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_listing_data(self):
        self.driver.find_element_by_link_text("Your Feed").click()
        your_feed = self.driver.find_elements_by_class_name("author")
        assert len(your_feed) > 0
        print("Az oldalon levő bejegyzések száma: ", len(your_feed))
