# -*- coding: utf-8 -*-
#Step 1 ==> 下載 chromedriver.exe，並把執行檔路徑記下來
#Step 2 ==> pip install selenium

from selenium import webdriver
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www19.eyny.com/forum-205-1.html")

driver.find_element_by_xpath("""//*[@id="wp"]/table[4]/tbody/tr[1]/td[3]/a""").click()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://hinet.xervice.in/login/auth")


username = driver.find_element_by_xpath("""//*[@id="username"]""")
password = driver.find_element_by_xpath("""//*[@id="password"]""")
username.send_keys("doublekai0904@gmail.com")
password.send_keys("1111")
login_attempt = driver.find_element_by_xpath("""//*[@id="loginForm"]/a[1]""")
login_attempt.submit()

time.sleep(10)


