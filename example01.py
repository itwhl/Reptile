import random
import re
import time

import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        }
    )
    pattern = re.compile(r'\<span class="title"\>(.*?)\<\/span\>')
    results = pattern.findall(resp.text)
    results = [result for result in results if not result.startswith('&nbsp;')]
    for result in results:
        print(result)
    time.sleep(random.randint(1, 3))
