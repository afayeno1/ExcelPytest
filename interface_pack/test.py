from selenium import webdriver

# 设置浏览器选项
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
# driver.maximize_window()
# driver.implicitly_wait(3)