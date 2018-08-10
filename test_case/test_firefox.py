# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class FireFox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://start.firefoxchina.cn/"
        self.verificationErrors = [] 
        self.accept_next_alert = True
    
    def test_firefox(self): 
        u"""Firefox搜索用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("search-key").clear()
        driver.find_element_by_id("search-key").send_keys("selenium webdriver")
        driver.find_element_by_id("search-submit").click()
        time.sleep(5)
   
    def tearDown(self):
        self.driver.quit()
        
# unitest.main()函数用来测试 类中以 test 开头的测试用例
if __name__ == "__main__":
    unittest.main()
