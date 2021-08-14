import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.headless = True


class TestMultiplePages(object):
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
        self.driver.find_element(By.LINK_TEXT, "conduit").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_multiple_pages(self):
        self.driver.find_element_by_link_text("Your Feed").click()
        time.sleep(1)
        page_link = self.driver.find_elements_by_class_name("page-link")
        fpa = []
        for i in range(len(page_link)):
            feed_pages_article = self.driver.find_elements_by_class_name("article-preview")
            assert len(feed_pages_article) > 0
            print(f"Az {i+1}.oldalon levő bejegyzések száma: ", len(feed_pages_article))
            fpa.append(feed_pages_article[0].find_element_by_xpath('//a/h1').text)
            if i > 0:
                assert fpa[i] != fpa[i-1]
            if i < len(page_link)-1:
                self.driver.find_element_by_xpath(f'//a[@class="page-link"][text()="{i+2}"]').click()
            time.sleep(3)
