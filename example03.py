import random
import time

from lxml import etree
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    # 使用XML的XPath语法解析页面
    tree = etree.HTML(resp.text)
    spans = tree.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))
