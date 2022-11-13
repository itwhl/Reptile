import time
import datetime
import requests
from lxml import etree

from database import db_session_factory
from gongshangmodels import GongShangXinXi

now_time = datetime.datetime.now()


def generate_cookies():
    cookies_info = 'jsid=SEO-GOOGLE-ALL-SY-000001; TYCID=f0ea3a10ecfb11eabe9a1f21eeffe700; ssuid=5141147115; _ga=GA1.2.1553036628.1599037745; _gid=GA1.2.1050237828.1599037745; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1MDIwNDAwMyIsImlhdCI6MTU5OTExMDQ4NSwiZXhwIjoxNjMwNjQ2NDg1fQ.6T6l9oNhK9GwmI3bwBSEhjmin9Ei5cnyKnxZxGCKsrWyV6Fbfu5UCv1N8YaH-GsdgfuRJP1c-I4v9U9bIwB0tQ; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522personalClaimType%2522%253A%2522none%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522score%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522showPost%2522%253Anull%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1MDIwNDAwMyIsImlhdCI6MTU5OTExMDQ4NSwiZXhwIjoxNjMwNjQ2NDg1fQ.6T6l9oNhK9GwmI3bwBSEhjmin9Ei5cnyKnxZxGCKsrWyV6Fbfu5UCv1N8YaH-GsdgfuRJP1c-I4v9U9bIwB0tQ%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522scoreUnit%2522%253A%2522%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myTidings%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%25B0%25A2%25E9%2580%258A%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522bossStatus%2522%253A%25222%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522yellowDiamondEndTime%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522yellowDiamondStatus%2522%253A%2522-1%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213550204003%2522%257D; tyc-user-phone=%255B%252213550204003%2522%255D; aliyungf_tc=AQAAAA1NbX+LbgwAzXd6dpuns2DMErF2; csrfToken=fK8AZrZb1s_xkSr70M1bPhX9; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1599037744,1599110451,1599190760; RTYCID=2a5c42716be04ed4ab63e1557f9c3a45; CT_TYCID=ab29631cc3cc4531806c9b4fbca14011; token=b3d62997c1be42b2bd8257af6900ca64; _utm=3111241114a44ea08cba37174b0c29aa; cloud_token=14f892aec33d49f1b4cc789feb9f8349; cloud_utm=973f422e1487483a96b17e8e65b7f52e; _gat_gtag_UA_123487620_1=1; relatedHumanSearchGraphId=150041670; relatedHumanSearchGraphId.sig=V_xNExPxa3iV1Xti946DJxIHH7XYPnhwIkXOqne0H2k; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1599194608'
    cookies = {}
    for item in cookies_info.split(';'):
        key, value = item.strip().split('=', maxsplit=1)
        cookies[key] = value
    return cookies


def resp_url(url):
    resp = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'},
        cookies=generate_cookies()
    )
    return resp.text


# 翻页
for page in range(5, 6):
    time.sleep(6)
    resp = requests.get(
        url=f'https://www.tianyancha.com/search/p{page}?key=%E6%96%B0%E7%96%86%E5%85%AC%E5%8F%B8',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'},
        cookies=generate_cookies()
    )
    # 开始请求所有公司链接页面
    tree = etree.HTML(resp.text)
    for i in range(1, 21):
        time.sleep(3)
        span_url = tree.xpath(f'//*[@id="web-content"]/div/div[1]/div[3]/div[2]/div[{i}]/div/div[3]/div[1]/a/@href')
        # 开始请求每个公司的详情页
        for url in span_url:
            tree_url = etree.HTML(resp_url(url))
            span_name = tree_url.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[1]/h1/text()')
            name = span_name[0]
            span_xinyongdaima = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[2]/text()')
            daima = span_xinyongdaima[0]
            span_zhucehao = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[4]/text()')
            zhucehao = span_zhucehao[0]
            span_zhucezijin = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]/div/text()')
            zhucezijin = span_zhucezijin[0]
            span_shijiaoziben = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[4]/text()')
            shijiaoziben = span_shijiaoziben[0]
            span_chengliriqi = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]/div/text()')
            chengliriqi = span_chengliriqi[0]
            span_faren = tree_url.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div/div[1]/div[2]/div[1]/a/text()')
            faren = span_faren[0]
            span_jingyingzhuangtai = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[4]/text()')
            jingyinghzuangtai = span_jingyingzhuangtai[0]
            span_gsleixing = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[2]/text()')
            gsleixing = span_gsleixing[0]
            span_gshangye = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]/text()')
            gshangye = span_gshangye[0]
            span_jiguan = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[4]/text()')
            jiguan = span_jiguan[0]
            span_dizhi = tree_url.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[10]/td[2]/text()')
            dizhi = span_dizhi[0]

        # 储存到数据库
        model = GongShangXinXi(gs_name=name, falv_ren=faren, chengli_riqi=chengliriqi, jy_status=jingyinghzuangtai, gs_type=gsleixing,gs_hangye=gshangye, dj_jiguan=jiguan, zc_dizhi=dizhi, xinyong_daima=daima,gs_zhucehao=zhucehao, zc_ziben=zhucezijin, sj_ziben=shijiaoziben, )
        session = db_session_factory()
        session.add(model)
        session.commit()


        # print(f'公司名称:{name},  法定代表人:{faren}, 成立日期:{chengliriqi}, 经营状态:{jingyinghzuangtai}, 公司类型:{gsleixing},  公司行业:{gshangye}, 登记机关:{jiguan}, 注册地址:{dizhi}, 统一社会信用代码:{daima}, 工商注册号:{zhucehao}, 注册资本:{zhucezijin}, 实缴资本:{shijiaoziben}')