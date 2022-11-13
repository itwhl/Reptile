from lxml import etree
import requests

resp = requests.get(
    url=f'https://movie.douban.com/top250',
    headers={
        'User-Agent': 'BaiduSpider',
    }
)
# 使用XML的XPath语法解析页面
tree = etree.HTML(resp.text)
hrefs = tree.xpath('//a[@href]/@href')
for href in hrefs:
    print(href)
