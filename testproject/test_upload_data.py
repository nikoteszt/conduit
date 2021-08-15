import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True


class TestUploadData(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:1667/")
        time.sleep(3)
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testuser3@example.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Abcd123$")
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(3)
        assert len(self.driver.find_elements_by_link_text('testuser3')) > 0

    def teardown_method(self):
        self.driver.find_element_by_link_text("conduit").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Log out").click()
        self.driver.close()
        self.driver.quit()

    def test_upload_data(self):
        g_feed = self.driver.find_elements_by_class_name("article-preview")
        feed_upload = 0
        with open('./upload_data.csv', encoding="utf-8") as ud_file:
            csv_reader = csv.reader(ud_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                self.driver.find_element(By.XPATH, "//a[contains(text(),\'New Article\')]").click()
                time.sleep(3)
                self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(row[0])
                self.driver.find_element_by_xpath('//fieldset[2]/input').send_keys(row[1])
                self.driver.find_element_by_xpath('//li/input').send_keys(row[2])
                self.driver.find_element_by_xpath('//textarea').send_keys(row[3])
                self.driver.find_element_by_xpath('//button[@type="submit"]').click()
                time.sleep(3)
                feed_upload += 1
        ud_file.close()
        self.driver.find_element_by_link_text("Home").click()
        time.sleep(3)
        g_feed_after_upload = self.driver.find_elements_by_class_name("article-preview")
        assert len(g_feed_after_upload) == len(g_feed) + feed_upload
