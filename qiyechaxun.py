import time

import requests
from lxml import etree


def generate_cookies():
    cookies_info = 'jsid=SEO-GOOGLE-ALL-SY-000001; TYCID=f0ea3a10ecfb11eabe9a1f21eeffe700; ssuid=5141147115; _ga=GA1.2.1553036628.1599037745; _gid=GA1.2.1050237828.1599037745; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1MDIwNDAwMyIsImlhdCI6MTU5OTExMDQ4NSwiZXhwIjoxNjMwNjQ2NDg1fQ.6T6l9oNhK9GwmI3bwBSEhjmin9Ei5cnyKnxZxGCKsrWyV6Fbfu5UCv1N8YaH-GsdgfuRJP1c-I4v9U9bIwB0tQ; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522personalClaimType%2522%253A%2522none%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522score%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522showPost%2522%253Anull%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1MDIwNDAwMyIsImlhdCI6MTU5OTExMDQ4NSwiZXhwIjoxNjMwNjQ2NDg1fQ.6T6l9oNhK9GwmI3bwBSEhjmin9Ei5cnyKnxZxGCKsrWyV6Fbfu5UCv1N8YaH-GsdgfuRJP1c-I4v9U9bIwB0tQ%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522scoreUnit%2522%253A%2522%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myTidings%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%25B0%25A2%25E9%2580%258A%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522bossStatus%2522%253A%25222%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522yellowDiamondEndTime%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522yellowDiamondStatus%2522%253A%2522-1%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213550204003%2522%257D; tyc-user-phone=%255B%252213550204003%2522%255D; aliyungf_tc=AQAAAA1NbX+LbgwAzXd6dpuns2DMErF2; csrfToken=fK8AZrZb1s_xkSr70M1bPhX9; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1599037744,1599110451,1599190760; RTYCID=2a5c42716be04ed4ab63e1557f9c3a45; CT_TYCID=ab29631cc3cc4531806c9b4fbca14011; token=b3d62997c1be42b2bd8257af6900ca64; _utm=3111241114a44ea08cba37174b0c29aa; cloud_token=14f892aec33d49f1b4cc789feb9f8349; cloud_utm=973f422e1487483a96b17e8e65b7f52e; _gat_gtag_UA_123487620_1=1; relatedHumanSearchGraphId=150041670; relatedHumanSearchGraphId.sig=V_xNExPxa3iV1Xti946DJxIHH7XYPnhwIkXOqne0H2k; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1599194608'
    cookies = {}
    for item in cookies_info.split(';'):
        key, value = item.strip().split('=', maxsplit=1)
        cookies[key] = value
    return cookies


for page in range(1, 6):
    time.sleep(5)
    resp = requests.get(
        url=f'https://www.tianyancha.com/search/p{page}?key=%E5%9B%9B%E5%B7%9D%E5%85%AC%E5%8F%B8',
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'},
        cookies=generate_cookies()
    )
    tree = etree.HTML(resp.text)
    for i in range(1, 21):
        time.sleep(2)
        span_title = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/em[1]/text() | //*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/em[2]/text() | //*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/text() | //*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/text()[2] | //*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/em[3]/text()')
        title = ''.join(span_title)
        # print(title)
        span_faren = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[3]/div[1]/a/text()')
        faren = ''.join(span_faren)
        # print(faren)
        span_login_fund = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[3]/div[2]/span/text()')
        login_fund = ''.join(span_login_fund)
        # print(login_fund)
        span_setup_date = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[3]/div[3]/span/text()')
        setup_date = ''.join(span_setup_date)
        # print(setup_date)
        span_tel = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[4]/div[1]/span[2]/span[1]/text()')
        tel = ''.join(span_tel)
        # print(tel)

        print(f'公司名称:{title}, 法律代表人:{faren}, 注册成本:{login_fund}, 成立日期:{setup_date}, 电话:{tel}')