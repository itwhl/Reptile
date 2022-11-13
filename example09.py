"""
抓取动态内容
方法1：JavaScript逆向
"""
from concurrent.futures.thread import ThreadPoolExecutor

import requests


def download_picture(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        filename = url[url.rfind('/') + 1:]
        with open(f'images/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    with ThreadPoolExecutor(max_workers=16) as pool:
        for num in range(0, 100, 10):
            resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={num}&listtype=new&temp=1')
            result = resp.json()
            for data in result['list']:
                pool.submit(download_picture, data['imgurl'])


if __name__ == '__main__':
    main()
