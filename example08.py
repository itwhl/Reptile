"""
IP代理池 - 隐匿爬虫的真实IP地址，预防爬虫程序被封禁IP
"""
import time

import bs4
import requests

from database import db_session_factory
from models import DoubanMovie


def generate_cookies():
    cookies_info = '请填写自己浏览器里面拿到的cookie信息'
    cookies = {}
    for item in cookies_info.split(';'):
        key, value = item.strip().split('=', maxsplit=1)
        cookies[key] = value
    return cookies


def fetch_page(url):
    resp = requests.get(
        url=url,
        # 通过设置请求头冒充浏览器
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                          'Safari/537.36',
        },
        # 通过在请求中添加cookie信息冒充登录过的用户（可以创建Cookie池随机选择Cookie信息）
        cookies=generate_cookies(),
    )
    return resp.text


def get_movie_detail(url):
    html_code = fetch_page(url)
    soup = bs4.BeautifulSoup(html_code, 'lxml')
    div = soup.select_one('#info')
    category_spans = div.select('span[property="v:genre"]')
    category = ''
    for index, span in enumerate(category_spans):
        category += span.text
        if index < len(category_spans) - 1:
            category += ' / '
    spans = div.select('#info > span.pl')
    country = spans[1].next_sibling.strip()
    language = spans[2].next_sibling.strip()
    duration_span = div.select_one('span[property="v:runtime"]')
    duration = duration_span.attrs['content']
    return category, country, language, duration


def main():
    for page in range(1, 11):
        html_code = fetch_page(f'https://movie.douban.com/top250?start={(page - 1) * 25}')
        soup = bs4.BeautifulSoup(html_code, 'lxml')
        divs = soup.select('div.info')
        for div in divs:
            # 获取电影详情链接的href属性
            anchor = div.select_one('div.hd > a')
            detail_url = anchor.attrs['href']
            # 通过详情页获取电影的分类、国家、语言、时长信息
            category, country, language, duration = get_movie_detail(detail_url)
            # 获取电影的标题、评分和名言信息
            title = anchor.select_one('span:first-Child').text
            rank = div.select_one('div.bd > div.star > span.rating_num').text
            motto_span = div.select_one('div.bd > p.quote > span')
            motto = motto_span.text if motto_span else ''
            model = DoubanMovie(title=title, rank=rank, motto=motto,
                                category=category, country=country,
                                language=language, duration=duration)
            session = db_session_factory()
            session.add(model)
            session.commit()
        time.sleep(5)


if __name__ == '__main__':
    main()
