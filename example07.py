"""
解析搜狐首页的超链接（标题，href属性）
"""
import re
from urllib.parse import urljoin

# import bs4
import requests

resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    pattern = re.compile(r'<a\s+.*?href="(.*?)".*?>(.*?)</a>')
    results = pattern.findall(resp.text)
    for result in results:
        content = re.sub(r'(\s)|(<.*?>)|(</.*?>|(&.*?;))', '', result[1])
        url = urljoin('http://', result[0])
        if content:
            print(f'{content}: {url}')
    # soup = bs4.BeautifulSoup(resp.text, 'lxml')
    # //a[@href]/@href
    # all_anchors = soup.select('a[href]')
    # for anchor in all_anchors:
    #     content = re.sub(r'\s', '', anchor.text)
    #     url = urljoin('http://', anchor.attrs['href'])
    #     if content:
    #         print(f'{content}: {url}')
