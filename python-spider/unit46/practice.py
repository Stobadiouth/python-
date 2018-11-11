from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
# chrome_options.add_argument('--enable-logging')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

try:
    browser=webdriver.Chrome(options=chrome_options)
    browser.get("http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=0&province=%E6%B1%9F%E8%8B%8F&city=0&marriage=0&edu=0&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0")
    #等待页面加载
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'search_box')))
    current_window = browser.current_window_handle  # 获取当前窗口handle name
    #获取所有有超链接的图片
    links=browser.find_elements_by_class_name('lazy')
    print(len(links))
    for i in range(len(links)):
        links[i].click()
        all_windows = browser.window_handles  # 获取所有窗口handle name
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                browser.switch_to.window(window)
        browser.implicitly_wait(10)
        with open('user{0}.html'.format(i),'w',encoding='utf-8') as fp:
            fp.write(browser.page_source)
            fp.close()

        browser.close()
        browser.switch_to.window(current_window)  # 关闭新窗口后切回原窗口，在这里不切回原窗口，是无法操作原窗口元素

except Exception as ex:
    print(ex)

finally:
    browser.close()