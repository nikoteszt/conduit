import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.headless = True
# TC07, TC08, TC09


class TestPostSuite(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:1667/#/")
        time.sleep(2)
        self.driver.find_element_by_link_text("Sign in").click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("ntest2@ceg.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("ntest222A")
        self.driver.find_element_by_class_name("btn-primary").click()

    def teardown_method(self):
        self.driver.find_element_by_link_text("conduit").click()
        self.driver.find_element_by_link_text("Log out").click()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_tc07_new_post(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),\'New Article\')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("Első_saját")
        self.driver.find_element(By.XPATH, "//fieldset[2]/input").send_keys("He")
        self.driver.find_element(By.XPATH, "//textarea").send_keys(
            "Ez itt most az első posztom. Sok minden nem fér bele. Vagy mégis?")
        self.driver.find_element(By.XPATH, "//li/input").send_keys("első")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Your Feed").click()
        my_post = self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Első_saját\')]")
        assert len(my_post) > 0
        time.sleep(2)

    def test_tc08_edit_post(self):
        new_tag = "update"
        time.sleep(2)
        posts = self.driver.find_elements_by_class_name("preview-link")
        # posts_tag = self.driver.find_elements_by_xpath('//div[@class="tag-list"]')
        # post_tags = len(posts_tag[-2].find_elements_by_xpath('//a'))
        # print(post_tags)
        # print(posts_tag[-2].find_element_by_xpath('//a').text)
        posts[-1].click()
        time.sleep(2)
        self.driver.find_element_by_class_name("ion-edit").click()
        time.sleep(2)
        self.driver.find_element_by_tag_name("textarea").send_keys(" Bővítjük a posztomat.")
        self.driver.find_element_by_xpath('//li/input').send_keys(new_tag)
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Home").click()
        time.sleep(2)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        # print(len(posts_tag[-2].find_elements_by_xpath('//a')))
        # print(posts_tag[-2].find_element_by_xpath('//a').text)
        # assert posts_tag[-2].find_element_by_xpath('/a[1]').text == new_tag
        time.sleep(2)

    def test_tc09_del_post(self):
        time.sleep(2)
        your_feed_num = len(self.driver.find_elements_by_class_name("author"))
        posts = self.driver.find_elements_by_xpath('//div[@class="tag-list"]')
        posts[-2].click()
        time.sleep(2)
        self.driver.find_element_by_class_name("ion-trash-a").click()
        time.sleep(2)
        assert len(self.driver.find_elements_by_class_name("author")) == your_feed_num - 1
