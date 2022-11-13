"""
IP代理池 - 隐匿爬虫的真实IP地址，预防爬虫程序被封禁IP
"""
import random
import re

import redis
import requests


class NoProxiesError(Exception):
    pass


def update_proxies_pool():
    """通过蘑菇代理获取代理服务器地址和端口，构建IP代理池"""
    proxies_pool = []
    resp = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_bs'
                        '?appKey=4338998cd0824d9d9d75f8905bd687ba&count=5&'
                        'expiryDate=0&format=1&newLine=2')
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '0':
            for item in result['msg']:
                ip, port = item['ip'], item['port']
                proxies_pool.append(f'http://{ip}:{port}')
            return proxies_pool
    raise NoProxiesError('获取代理服务器信息失败，请重试！！！')


def main():
    # 通过Redis的列表类型作为IP代理池并设置过期时间
    redis_cli = redis.Redis(host='47.104.31.138', port=5489, password='Luohao.618', db=15)
    for page in range(1, 11):
        proxies_pool = redis_cli.lrange('proxies_pool', 0, -1)
        # 如果Redis中获取不到IP代理池，那么就重新获取一组IP代理并构建代理池
        if not proxies_pool:
            proxies_pool = update_proxies_pool()
            for proxy in proxies_pool:
                redis_cli.rpush('proxies_pool', proxy)
            redis_cli.expire('proxies_pool', 60)
            proxies_pool = redis_cli.lrange('proxies_pool', 0, -1)
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            # 通过设置请求头冒充浏览器
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 '
                              'Safari/537.36',
            },
            # 设置通过代理服务器代理获取页面的请求
            proxies={'http': random.choice(proxies_pool).decode()}
        )
        pattern = re.compile(r'\<span class="title"\>(.*?)\<\/span\>')
        results = pattern.findall(resp.text)
        results = [result for result in results if not result.startswith('&nbsp;')]
        for result in results:
            print(result)


if __name__ == '__main__':
    main()
