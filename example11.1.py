"""
抓取动态图片方法二

"""
import time
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from lxml import etree
from selenium import webdriver


def download_picture(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        filename = url[url.rfind('/') + 1:]
        with open(f'D:/Users/Desktop/image/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    with ThreadPoolExecutor(max_workers=16) as pool:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        # 指定每次加载页面时要执行的JavaScript脚本代码
        # 通过将window.navigation.webdriver属性修改为undefined来绕过对selenium的检查
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
        })
        driver.maximize_window()
        driver.get('http://image.so.com/')
        search_kw_input = driver.find_element_by_id('search_kw')
        search_kw_input.send_keys('斗图')
        search_button = driver.find_element_by_css_selector('button[type=submit]')
        search_button.click()
        scroll_top = 800
        for i in range(1, 31):
            time.sleep(1.6)
            driver.execute_script(f'window.scrollTo(0, {scroll_top * i})')
        tree = etree.HTML(driver.page_source)
        urls = tree.xpath('//*[@id="searchlist"]/div[1]/ul/li/div/a[1]/span[1]/img/@src')
        for url in urls:
            pool.submit(download_picture, url)


if __name__ == '__main__':
    main()