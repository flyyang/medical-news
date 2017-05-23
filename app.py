# encoding=utf-8
import time
import spider
from wechat import WeChat

def main():
    wc = WeChat()
    spider_man = {
        "hc3i": "",
        "iyiou": "",
        "sina": "",
        "hchina": "",
        "vcbeat": "",
        "ckxx": "",
        "xinhua": "",
        "biodiscover": "",
    }
    site_map = {
        "hc3i": "中国数字医疗网",
        "iyiou": "亿欧",
        "sina": "新浪医药",
        "hchina": "健康中国",
        "vcbeat": "动脉网",
        "ckxx": "参考消息",
        "xinhua": "新华健康",
        "biodiscover": "生物探索",
    }
    while True:
        for item in spider_man:
            spider_res = getattr(spider, item)()
            if spider_man[item] and spider_man[item] != spider_res["title"]:
                print "new post"
                wc.send('【' + site_map[item] + '】' + spider_res['title'],
                        spider_res['preview'],
                        spider_res['url'])
            spider_man[item] = spider_res["title"]

        time.sleep(30)
        print "new loop"


if __name__ == '__main__':
    main()
