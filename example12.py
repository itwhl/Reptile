import asyncio
import re

import aiohttp
import uvloop

PATTERN = re.compile(r'<title>(?P<foo>.*?)</title>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('foo'))


def main():
    urls = (
        'https://python.org/', 'https://git-scm.com/',
        'https://www.jd.com/', 'https://www.sohu.com',
        'https://www.taobao.com/', 'http://qq.com',
        'https://image.so.com', 'http://www.youku.com',
        'https://www.kaggle.com', 'http://tianchi.aliyun.com'
    )
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    print(tasks)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
