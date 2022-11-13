import time

import requests
from lxml import etree


for page in range(1,101):
    time.sleep(5)
    resp = requests.get(
        url=f'https://search.jd.com/Search?keyword=%E6%9D%9C%E8%95%BE%E6%96%AF&qrst=1&wq=%E6%9D%9C%E8%95%BE%E6%96%AF&stock=1&ev=exbrand_%E6%9D%9C%E8%95%BE%E6%96%AF%EF%BC%88durex%EF%BC%89%5E&page={page}',
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'},
    )
    tree = etree.HTML(resp.text)
    for i in range(1,31):
        time.sleep(2)
        span_jiage = tree.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[2]/strong/i/text()')
        jiage = ''.join(span_jiage)
        span_title = tree.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[3]/a/em/font/text()|//*[@id="J_goodsList"]/ul/li[{i}]/div/div[3]/a/em/text()')
        span_title = ''.join(span_title)
        title = str(span_title).replace(r'\t\n', '')
        print(f'{title}￥{jiage}')
