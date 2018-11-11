from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

browser=webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://www.baidu.com ")
input=browser.find_element_by_id('kw')
input.send_keys('python')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID,"content_left")))
with open('python.html','w',encoding='utf-8') as fp:
    fp.write(browser.page_source)
# print(browser.page_source)
# browser.close()