"""
抓取动态内容
方法2：通过Python程序控制浏览器获取动态内容
"""
import time

from lxml import etree
from selenium import webdriver

options = webdriver.ChromeOptions()
# 设置使用无头浏览器（没有运行浏览器界面）
# options.add_argument('-headless')
driver = webdriver.Chrome(options=options)
# 指定每次加载新页面时要执行的JavaScript脚本代码
# 通过将window.navigator.webdriver属性修改为undefined来绕过对Selenium的检查
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
driver.maximize_window()
driver.get('https://image.so.com/')
search_kw_input = driver.find_element_by_id('search_kw')
search_kw_input.send_keys('苍老师')
search_button = driver.find_element_by_css_selector('button[type=submit]')
search_button.click()
scroll_top = 800
for i in range(1, 31):
    time.sleep(1.6)
    driver.execute_script(f'window.scrollTo(0, {scroll_top * i})')
tree = etree.HTML(driver.page_source)
urls = tree.xpath('//*[@id="searchlist"]/div[1]/ul/li/div/a[1]/span[1]/img/@src')
for url in urls:
    print(url)
