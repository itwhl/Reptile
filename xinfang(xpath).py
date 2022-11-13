import time

import requests
from lxml import etree


for page in range(1, 10):
    time.sleep(1)
    resp = requests.get(
        url=f'https://cd.fang.lianjia.com/loupan/pg{page}/',
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'},
    )
    tree = etree.HTML(resp.text)
    for i in range(1, 11):
        time.sleep(1)
        span_title = tree.xpath(f'/html/body/div[4]/ul[2]/li[{i}]/div/div[1]/a/text()')
        span_totalprice = tree.xpath(f'/html/body/div[4]/ul[2]/li[{i}]/div/div[6]/div[2]/text()')
        span_danjia = tree.xpath(f'/html/body/div[4]/ul[2]/li[{i}]/div/div[6]/div[1]/span[1]/text()')
        span_area = tree.xpath(f'/html/body/div[4]/ul[2]/li[{i}]/div/div[2]/span/text() | /html/body/div[4]/ul[2]/li[{i}]/div/div[2]/a/text()')
        span_huxing = tree.xpath(f'/html/body/div[4]/ul[2]/li[{i}]/div/a/span/text() | /html/body/div[4]/ul[2]/li[{i}]/div/div[3]/span/text()')
        print(f'小区:{span_title}, 户型:{span_huxing}, 面积:{span_area}, 单价:{span_danjia}元/㎡, 总价:{span_totalprice}')
