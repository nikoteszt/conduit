# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("http://localhost:1667/")
    self.driver.set_window_size(918, 824)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("ntest2@ceg.hu")
    self.driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("ntest222A")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Sign in\')]").click()
    assert self.driver.find_element(By.LINK_TEXT, "ntest2").text == "ntest2"
  