# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class FirefoxSetting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://start.firefoxchina.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_firefox_setting(self):
        u"""Firefox皮肤设置用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"火狐主页").click()
        driver.find_element_by_xpath("//div[@id='btn-system-skin']/p/span").click()
        driver.find_element_by_xpath("//div[@id='sd-skin']/div/div/div/div/ul/li[5]/div/img").click()
        driver.find_element_by_css_selector("div.mod-action.skin-action > input.btn.btn-confirm").click()
        time.sleep(5)
    
    def tearDown(self):
        #Driver.time(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
