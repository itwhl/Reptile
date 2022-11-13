"""
抓取动态内容
方法2：通过Python程序控制浏览器获取动态内容
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 创建Chrome浏览器驱动
driver = webdriver.Chrome()
# 设置浏览器窗口最大化
driver.maximize_window()
# 加载百度首页
driver.get('https://www.baidu.com')
# 获取页面上输入搜索关键字的文本框
kw_input = driver.find_element_by_id('kw')
# 模拟输入Python关键字
kw_input.send_keys('骆昊')
# 获取页面上的搜索按钮
su_button = driver.find_element_by_id('su')
# 模拟点击按钮
su_button.click()
try:
    # 等待搜索结果出现（id为content_left的div里面是搜索结果）
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'content_left')
        )
    )
    # 屏幕截图
    driver.get_screenshot_as_file('baidu-python-index.png')
finally:
    # 退出
    driver.quit()
