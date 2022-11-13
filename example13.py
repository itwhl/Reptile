import re

import requests

PATTERN = re.compile(r'<title>(?P<title>.*?)</title>')


def main():
    urls = (
        'https://python.org/', 'https://git-scm.com/',
        'https://www.jd.com/', 'https://www.sohu.com',
        'https://www.taobao.com/', 'http://qq.com',
        'https://image.so.com', 'http://www.youku.com',
        'https://www.kaggle.com', 'http://tianchi.aliyun.com'
    )
    for url in urls:
        resp = requests.get(url, timeout=30)
        print(PATTERN.search(resp.text).group('title'))


if __name__ == '__main__':
    main()
