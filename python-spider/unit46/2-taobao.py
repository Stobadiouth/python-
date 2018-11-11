from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import requests

chrome_options=Options()
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

try:
    browser=webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://s.taobao.com/search?q=nike&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2018.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306")
    goods=browser.find_elements_by_class_name('J_ClickStat')
    current_window = browser.current_window_handle  # 获取当前窗口handle name

    wait=None
    for i in range(2):
        # 点击查找
        goods[i].click()
        wait=WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.ID,"attributes")))
        all_windows = browser.window_handles  # 获取所有窗口handle name
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                browser.switch_to.window(window)
        with open('good{0}.html'.format(i),'w',encoding='utf-8') as fp:
            fp.write(browser.page_source)
            fp.close()
        browser.back()
        time.sleep(2)

        #获取连接查找
        # with requests.get(url=goods[i].get_attribute('href')) as response:
        #     data=response.text
        #     with open('good{0}.html'.format(i),'w',encoding='utf-8') as fp:
        #         fp.write(data)
        #         fp.close()
except Exception as ex:
    print(ex)
finally:
    browser.close()