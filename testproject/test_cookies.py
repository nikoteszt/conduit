import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.headless = True
# TC04


class TestCookies(object):
    def setup_method(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:1667/")
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_cookies_accept(self):
        def login():
            self.driver.find_element_by_link_text("Sign in").click()
            self.driver.find_element_by_xpath('//input[@type="text"]').send_keys("ntest2@ceg.hu")
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys("ntest222A")
            self.driver.find_element_by_class_name("btn-primary").click()
            time.sleep(2)

        def logout():
            self.driver.find_element_by_link_text("conduit").click()
            self.driver.find_element_by_link_text("Log out").click()

        def cookies_checker():
            time.sleep(2)
            assert not len(
                self.driver.find_elements_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div'))

        # ellenőrizzük, hogy a cookie kezelést elfogadó gomb megjelenik e
        assert len(self.driver.find_elements_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')) > 0

        login()
        # elfogadjuk a kezelést, majd ellenőrizzük, hogy eltünt e a gomb
        self.driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()
        cookies_checker()

        # frissítjük az oldalt, és ismét ellenőrizzük, hogy a gomb nem tért vissza
        self.driver.refresh()
        cookies_checker()

        # kijelentkezünk, majd ismét bejelentkezünk, és ellenőrízzük, hogy a gomb továbbra sincs jelen.
        logout()
        time.sleep(2)
        login()
        cookies_checker()
