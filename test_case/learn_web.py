#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from common_module.web_keyword import Keyword

from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT,"更多")).perform()
Keyword().move_to_element(driver,"//div/a[text()='更多']")
sleep(2)
Keyword().click(driver,"//a/div[text()='学术']")
Keyword().switch_to_window(driver,"百度一下，你就知道")
# handles=driver.window_handles
# for handle in handles:
#     driver.switch_to.window(handle)
#     if driver.title=="百度一下，你就知道":
#         break
# print("error")
# driver.find_element(By.XPATH,"//a/div[text()='学术']").click()
# driver.find_element(By.LINK_TEXT,'登录').click()
Keyword().click(driver,'//div/a[@id="s-top-loginbtn"]')
# sleep(1)
# driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_11__userName']").send_keys("afayeno1")
Keyword().input(driver,"//*[@id='TANGRAM__PSP_11__userName']","afayeno1")
# driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_11__password']").send_keys("Leon@0808")
Keyword().input(driver,"//*[@id='TANGRAM__PSP_11__password']","Leon@0808")
# driver.find_element(By.XPATH,"//input[@name='isAgree']").click()
Keyword().click(driver,"//input[@name='isAgree']")
# sleep(1)
# driver.find_element(By.XPATH,"//input[@class='pass-button pass-button-submit']").click()
Keyword().click(driver,"//input[@class='pass-button pass-button-submit']")
# s=driver.find_element(By.XPATH,"//*[@id='dialogWrapper']/div/div/div/p[1]").text
Keyword().check(driver,"//*[@id='dialogWrapper']/div/div/div/p[1]",	"验证方式选择")
# print(s)

sleep(5)
driver.quit()