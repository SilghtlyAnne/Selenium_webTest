# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu(self):
        u"""百度搜索用例"""
        driver = self.driver
        driver.get(self.base_url + "/?tn=98012088_5_dg&ch=12")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("select")
        driver.find_element_by_id("su").click()
        time.sleep(3)
       
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
