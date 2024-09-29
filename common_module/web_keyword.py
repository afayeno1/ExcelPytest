#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import strftime, localtime
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Keyword:
    def get_screenshot(self,driver):
        path = '//screenShot'
        file_name = strftime('%Y%m%d%H%M%S', localtime()) + ".png"
        path = os.path.join(path, file_name)
        driver.get_screenshot_as_file(path)
        allure.attach.file("../screenShot/%s" % file_name, name="screeshot",
                           attachment_type=allure.attachment_type.JPG)

    def click(self,driver,element):
        try:
            driver.find_element(By.XPATH,element).click()
        except:
            self.get_screenshot(driver)
            raise AssertionError

    def input(self,driver,element,value):
        try:
            driver.find_element(By.XPATH,element).send_keys(value)
        except:
            self.get_screenshot(driver)
            raise AssertionError

    def move_to_element(self,driver,element):
        try:
            ActionChains(driver).move_to_element(driver.find_element(By.XPATH,element)).perform()
        except:
            self.get_screenshot(driver)
            raise AssertionError

    def switch_to_window(self,driver,title):
        try:
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
                if driver.title==title:
                    break
        except:
            self.get_screenshot(driver)
            raise AssertionError

    def open(self,driver,url):
        driver.get(url)

    def check(self,driver,element,text):
        try:
            assert driver.find_element(By.XPATH,element).text==text
        except:
            print(f"校验失败，实际值：{driver.find_element(By.XPATH,element).text}")
            self.get_screenshot(driver)
            raise AssertionError
