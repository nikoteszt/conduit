import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True


class TestSaveData(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:1667/")
        time.sleep(3)
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testuser1@example.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Abcd123$")
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(3)
        assert len(self.driver.find_elements_by_link_text('testuser1')) > 0

    def teardown_method(self):
        self.driver.find_element_by_link_text("conduit").click()
        self.driver.find_element_by_link_text("Log out").click()
        self.driver.close()
        self.driver.quit()

    def test_save_data(self):
        self.driver.find_element_by_xpath('(//li/a[@class="nav-link"])[3]').click()
        time.sleep(2)
        # articles = self.driver.find_elements_by_xpath('//div[@class="article-preview"]')
        articles = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')

        save_data = open("./save_data.txt", "w", encoding="utf-8")
        print("testuser1 blog bejegyzéseinek első oldala", file=save_data)
        print("", file=save_data)

        for i in range(len(articles)):
            print('Cím: ', articles[i].find_element_by_tag_name("h1").text, file=save_data)
            print('leírás: ', articles[i].find_element_by_tag_name("p").text, file=save_data)
            tags = articles[i].find_elements_by_xpath('//div[@class="tag-list"]/a')
            tag = ""
            for j in range(len(tags)):
                tag = tag + tags[j].text + ", "
            print('címkék: ', tag, file=save_data)
            print("", file=save_data)
        save_data.close()
